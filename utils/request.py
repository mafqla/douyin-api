# -*- encoding: utf-8 -*-
'''
@File    :   request.py
@Time    :   2024年07月15日
@Author  :   erma0
@Version :   1.1
@Link    :   https://github.com/ShilongLee/Crawler
@Desc    :   抖音sign
'''
import os
import random
import re
from urllib.parse import quote

import requests
from loguru import logger

from utils.cookies import get_cookie_dict
from utils.execjs_fix import execjs


class Request(object):
    HOST = 'https://www.douyin.com'
    LIVE_HOST = 'https://live.douyin.com'
    PARAMS = {
        'device_platform': 'webapp',
        'aid': '6383',
        'channel': 'channel_pc_web',
        'update_version_code': '170400',
        'pc_client_type': '1',  # Windows
        'version_code': '190500',
        'version_name': '19.5.0',
        'cookie_enabled': 'true',
        'screen_width': '2560',  # from cookie dy_swidth
        'screen_height': '1440',  # from cookie dy_sheight
        'browser_language': 'zh-CN',
        'browser_platform': 'Win32',
        'browser_name': 'Chrome',
        'browser_version': '126.0.0.0',
        'browser_online': 'true',
        'engine_name': 'Blink',
        'engine_version': '126.0.0.0',
        'os_name': 'Windows',
        'os_version': '10',
        'cpu_core_num': '24',  # device_web_cpu_core
        'device_memory': '8',  # device_web_memory_size
        'platform': 'PC',
        'downlink': '10',
        'effective_type': '4g',
        'round_trip_time': '50',
        # 'webid': '',   # from doc
        # 'verifyFp': '',   # from cookie s_v_web_id
        # 'fp': '', # from cookie s_v_web_id
        # 'msToken': '',  # from cookie msToken
        # 'a_bogus': '' # sign
    }
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "referer": "https://www.douyin.com/?recommend=1",
        "priority": "u=1, i",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "accept": "application/json, text/plain, */*",
        "dnt": "1",
    }
    filepath = os.path.dirname(__file__)
    SIGN = execjs.compile(
        open(os.path.join(filepath, '../lib/douyin.js'), 'r', encoding='utf-8').read())
    WEBID = ''

    def __init__(self, cookie='', UA=''):
        self.COOKIES = get_cookie_dict(cookie)
        if UA:  # 如果需要访问搜索页面源码等内容，需要提供cookie对应的UA
            version = UA.split(' Chrome/')[1].split(' ')[0]
            _version = version.split('.')[0]
            self.HEADERS.update({
                "User-Agent": UA,  # 主要是这个
                "sec-ch-ua": f'"Chromium";v="{_version}", "Not(A:Brand";v="24", "Google Chrome";v="{_version}"',
            })
            self.PARAMS.update({
                "browser_version": version,
                "engine_version": version,  # 主要是这个
            })

    def get_sign(self, uri: str, params: dict) -> dict:
        query = '&'.join([f'{k}={quote(str(v))}' for k, v in params.items()])
        call_name = 'sign_datail'
        if 'reply' in uri:
            call_name = 'sign_reply'
        a_bogus = self.SIGN.call(
            call_name, query, self.HEADERS.get("User-Agent"))
        return a_bogus

    def get_params(self, params: dict) -> dict:
        params.update(self.PARAMS)
        params['msToken'] = self.get_ms_token()
        params['screen_width'] = self.COOKIES.get('dy_swidth', 2560)
        params['screen_height'] = self.COOKIES.get('dy_sheight', 1440)
        params['cpu_core_num'] = self.COOKIES.get('device_web_cpu_core', 24)
        params['device_memory'] = self.COOKIES.get('device_web_memory_size', 8)
        params['verifyFp'] = self.COOKIES.get('s_v_web_id', None)
        params['fp'] = self.COOKIES.get('s_v_web_id', None)
        params['webid'] = self.get_webid()
        return params

    def get_webid(self):
        if not self.WEBID:
            url = 'https://www.douyin.com/?recommend=1'
            text = self.getHTML(url)
            pattern = r'\\"user_unique_id\\":\\"(\d+)\\"'
            match = re.search(pattern, text)
            if match:
                self.WEBID = match.group(1)
        return self.WEBID

    def get_ms_token(self, randomlength=120):
        """
        返回cookie中的msToken或随机字符串
        """
        ms_token = self.COOKIES.get('msToken', None)
        if not ms_token:
            ms_token = ''
            base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789='
            length = len(base_str) - 1
            for _ in range(randomlength):
                ms_token += base_str[random.randint(0, length)]
        return ms_token

    def getHTML(self, url) -> str:
        headers = self.HEADERS.copy()
        headers['sec-fetch-dest'] = 'document'
        response = requests.get(url, headers=headers, cookies=self.COOKIES)
        if response.status_code != 200 or response.text == '':
            logger.error(f'HTML请求失败, url: {url}, header: {headers}')
            return ''
        return response.text

    def getJSON(self, uri: str, params: dict, data: dict = None, live=None):
        url = f'{self.HOST}{uri}'
        live_url = f'{self.LIVE_HOST}{uri}'
        params = self.get_params(params)
        params["a_bogus"] = self.get_sign(uri, params)
        # 这个接口必须更改referer的值为当前请求页面的url
        referer_map = {
            '/aweme/v1/web/aweme/related/': f"https://www.douyin.com/video/{params.get('aweme_id')}",
            '/aweme/v1/web/comment/list/': f"https://www.douyin.com/video/{params.get('aweme_id')}",
            '/aweme/v1/web/comment/list/reply/': f"https://www.douyin.com/video/{params.get('item_id')}",
            '/aweme/v1/web/user/profile/other/': f"https://www.douyin.com/user/{params.get('sec_user_id')}?",
            '/aweme/v1/web/aweme/post/': f"https://www.douyin.com/user/{params.get('sec_user_id')}?",
            '/aweme/v1/web/im/spotlight/relation/': f"https://www.douyin.com/user/",
            '/aweme/v1/web/user/following/list/': f"https://www.douyin.com/user/",
            '/aweme/v1/web/user/follower/list/': f"https://www.douyin.com/user/",
            '/aweme/v1/web/aweme/favorite/': f"https://www.douyin.com/user/",
            '/aweme/v1/web/aweme/listcollection/': f"https://www.douyin.com/user/self?from_tab_name=main&showTab=favorite_collection",
            '/aweme/v1/web/music/listcollection/': f"https://www.douyin.com/user/self?from_tab_name=main&showSubTab=music&showTab=favorite_collection",
            '/aweme/v1/web/collects/video/list/': f"https://www.douyin.com/user/self?from_tab_name=main&showSubTab=favorite_folder&showTab=favorite_collection",
            '/aweme/v1/web/collects/list/': f"https://www.douyin.com/user/self?from_tab_name=main&showSubTab=favorite_folder&showTab=favorite_collection",
            '/aweme/v1/web/mix/listcollection/': f"https://www.douyin.com/user/self?from_tab_name=main&showSubTab=favorite_folder&showTab=favorite_collection",
            '/aweme/v1/web/series/collections': f"https://www.douyin.com/user/self?from_tab_name=main&showSubTab=favorite_folder&showTab=favorite_collection",
            '/aweme/v1/web/mix/list/': f"https://www.douyin.com/user/",
            '/aweme/v1/web/home/search/item/': f"https://www.douyin.com/user/",
            '/aweme/v1/web/seo/inner/link/': f"https://www.douyin.com/user/"
        }
        for pattern, referer_value in referer_map.items():
            if pattern == uri:
                self.HEADERS['referer'] = referer_value
                break
        if data:
            bd_client_data = self.COOKIES.get("bd_ticket_guard_client_data", None)
            self.HEADERS["Content-Type"] = "application/x-www-form-urlencoded"
            # self.HEADERS["Bd-Ticket-Guard-Client-Data"] = bd_client_data
            # self.HEADERS["Bd-Ticket-Guard-Web-Version"] = '1'
            # self.HEADERS["Bd-Ticket-Guard-Version"] = '2'
            # self.HEADERS["Bd-Ticket-Guard-Iteration-Version"] = '1'
            self.HEADERS["X-Secsdk-Csrf-Token"] = ''
            print(data)
            response = requests.post(
                url, params=params, data=data, headers=self.HEADERS, cookies=self.COOKIES)
            # print(f'url:{response.url}, header:{self.HEADERS}')
        elif live:
            response = requests.get(
                live_url, params=params, headers=self.HEADERS, cookies=self.COOKIES)
        else:
            response = requests.get(
                url, params=params, headers=self.HEADERS, cookies=self.COOKIES)
            # print(f'url:{response.url}, header:{self.HEADERS}')
        if response.status_code != 200 or response.text == '':
            logger.error(
                f'JSON请求失败：url: {url},  params: {params},header: {self.HEADERS}, code: {response.status_code}, body: {response.text}')
            return {}
        return response.json()


if __name__ == "__main__":
    r = Request()
    print(r.get_webid())
