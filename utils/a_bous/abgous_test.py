import pprint
import requests
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')  # 这三行代码需要放在导入execjs之前

import execjs
import urllib.parse

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    'cookie': '__live_version__=%221.1.1.709%22; ttwid=1%7CjBmBK11SMa_Y_r5LGdWYYwc7MNV29bKs5gA90kzfcsw%7C1716884485%7Cd85221bfe2573f01ebd078ece8cfdc27fd7298638eb7cdcd9c8c61626ab64137; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; dy_swidth=1847; dy_sheight=1039; s_v_web_id=verify_lwq4p1rd_x9KHBYiK_SAe5_4qyC_B58o_crG0hp49CNTn; csrf_session_id=4286063fbb0f225ea5c6025e45a8321b; strategyABtestKey=%221716884488.683%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; xgplayer_user_id=926508627749; passport_csrf_token=d149e11019361d4e653ce77a6dfd7f10; passport_csrf_token_default=d149e11019361d4e653ce77a6dfd7f10; xg_device_score=7.460496637831615; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; bd_ticket_guard_client_web_domain=2; my_rd=2; odin_tt=151912457e444897bb256ca92a206179323eab354ca543b2ec90e97b77cd2ce6bc0b0701e7a4eebded0c7f136b01a11dba7d9f60d92d5cc883c0af90128d1957841a1fdb0c5fe1f6d9256f02f4dd2f13; __ac_nonce=06655946f008a0f5b2d81; __ac_signature=_02B4Z6wo00f01Gb0UgAAAIDBSHOfKfatW7Bm1FaAAH.wCr3UzXYznqljrWsXMt7KQ7BRF8AmiJ5XApwycSkC9sJt2gC7l80m2NCgEVK-5VtBQE7t9eLDg7fpw2vVPTJ3Opeoc97ixdDfHoV493; SearchMultiColumnsVisitedTags=%5B%22for_discover_search-1%22%5D; SEARCH_RESULT_LIST_TYPE=%22multi%22; download_guide=%223%2F20240528%2F0%22; pwa2=%220%7C0%7C3%7C0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1847%2C%5C%22screen_height%5C%22%3A1039%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; WallpaperGuide=%7B%22showTime%22%3A1716884624149%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A0%2C%22cursor2%22%3A0%7D; home_can_add_dy_2_desktop=%220%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCR0krMHR2bmFnTm16RU1OQTdDMHhZa1ZhQ05FVWJ6UGFUYVVveEdNOGhCTTJZTk42UXhoRVhQU25seUZWOWZzMDZuR2xxWnZ6V0tQY2syK1l1a0tPSEE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=x8ILeHPHRaTNPtEQuILS3YdGPjUPx2Yzalj4DJsdNEEycaqPrNQROnaS4C8EIg95ZZ5eo5apI-J01HcjyOg-FqgG4PoczjmDtAjZCwmCUVrJDHualRyrChmxAfOqrk8=; IsDouyinActive=true',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAcdLig2KyRygH2j4SHpzwahXj7Cin6PDnFhOU4HwIHVx7UU65LAeOfQO267BxUdAZ',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAAcdLig2KyRygH2j4SHpzwahXj7Cin6PDnFhOU4HwIHVx7UU65LAeOfQO267BxUdAZ',  # 博主主页网址后半段路径就是ID
    # 'sec_user_id': 'MS4wLjABAAAADw1dDJd4zddv0m8KWQB7ztFV0Nt8QzIK7dpFvbsrXss',
    'max_cursor': '0',
    'locate_query': 'false',
    'show_live_replay_strategy': '1',
    'need_time_list': '1',
    'time_list_query': '0',
    'whale_cut_token': '',
    'cut_version': '1',
    'count': '18',
    'publish_video_strategy_type': '2',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'version_code': '290100',
    'version_name': '29.1.0',
    'cookie_enabled': 'true',
    'screen_width': '1847',
    'screen_height': '1039',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Chrome',
    'browser_version': '125.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '125.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '8',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '100',
    'webid': '7373962654656054793',
    'msToken': '_oAmCBg7EMDOt3T-1POfW1n6--0o-ASOEdZTCHgmLXSXk0HXBgM6rhfeUL7gQJFKgYt65DHDHpMzBx7IXRNj8sROdxFESJVCc_jDEcVIG1Pje7cJv29tel5uzx5GgFM=',
    'verifyFp': 'verify_lwq4p1rd_x9KHBYiK_SAe5_4qyC_B58o_crG0hp49CNTn',
    'fp': 'verify_lwq4p1rd_x9KHBYiK_SAe5_4qyC_B58o_crG0hp49CNTn',
}
search_headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    'cookie': '__live_version__=%221.1.1.709%22; ttwid=1%7CjBmBK11SMa_Y_r5LGdWYYwc7MNV29bKs5gA90kzfcsw%7C1716884485%7Cd85221bfe2573f01ebd078ece8cfdc27fd7298638eb7cdcd9c8c61626ab64137; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; dy_swidth=1847; dy_sheight=1039; s_v_web_id=verify_lwq4p1rd_x9KHBYiK_SAe5_4qyC_B58o_crG0hp49CNTn; csrf_session_id=4286063fbb0f225ea5c6025e45a8321b; strategyABtestKey=%221716884488.683%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; xgplayer_user_id=926508627749; passport_csrf_token=d149e11019361d4e653ce77a6dfd7f10; passport_csrf_token_default=d149e11019361d4e653ce77a6dfd7f10; xg_device_score=7.460496637831615; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; bd_ticket_guard_client_web_domain=2; my_rd=2; odin_tt=151912457e444897bb256ca92a206179323eab354ca543b2ec90e97b77cd2ce6bc0b0701e7a4eebded0c7f136b01a11dba7d9f60d92d5cc883c0af90128d1957841a1fdb0c5fe1f6d9256f02f4dd2f13; __ac_nonce=06655946f008a0f5b2d81; __ac_signature=_02B4Z6wo00f01Gb0UgAAAIDBSHOfKfatW7Bm1FaAAH.wCr3UzXYznqljrWsXMt7KQ7BRF8AmiJ5XApwycSkC9sJt2gC7l80m2NCgEVK-5VtBQE7t9eLDg7fpw2vVPTJ3Opeoc97ixdDfHoV493; SearchMultiColumnsVisitedTags=%5B%22for_discover_search-1%22%5D; SEARCH_RESULT_LIST_TYPE=%22multi%22; download_guide=%223%2F20240528%2F0%22; pwa2=%220%7C0%7C3%7C0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1847%2C%5C%22screen_height%5C%22%3A1039%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; WallpaperGuide=%7B%22showTime%22%3A1716884624149%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A0%2C%22cursor2%22%3A0%7D; home_can_add_dy_2_desktop=%220%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCR0krMHR2bmFnTm16RU1OQTdDMHhZa1ZhQ05FVWJ6UGFUYVVveEdNOGhCTTJZTk42UXhoRVhQU25seUZWOWZzMDZuR2xxWnZ6V0tQY2syK1l1a0tPSEE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=x8ILeHPHRaTNPtEQuILS3YdGPjUPx2Yzalj4DJsdNEEycaqPrNQROnaS4C8EIg95ZZ5eo5apI-J01HcjyOg-FqgG4PoczjmDtAjZCwmCUVrJDHualRyrChmxAfOqrk8=; IsDouyinActive=true',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/aweme/v1/web/general/search/single',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}
search = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'search_channel': 'aweme_general',
    'enable_history': '1',
    'keyword': '国防部官方发布第一条抖音',
    'search_source': 'hot_search_board',
    'query_correct_type': '1',
    'is_filter_search': '0',
    'from_group_id': '',
    'offset': '0',
    'count': '15',
    'need_filter_settings': 1,
    'list_type': 'single',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'version_code': '190600',
    'version_name': '19.6.0',
    'cookie_enabled': 'true',
    'screen_width': '1707',
    'screen_height': '1067',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Edge',
    'browser_version': '122.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '122.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '12',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '6.85',
    'effective_type': '4g',
    'round_trip_time': '200',
    'webid': '7321238709821998642',
    'msToken': '4LwDZ9tanGaUfZ7S4pJzPIY9iikffBIT4v46RIkkVMfBx_8yFZEo_DAH3Oa1X3P1iOVXou3JFrIl5Jv7XranNRbbEYjUJ_msKTVJKoqjfjXtCF3276X398Zfe1Dt1YXg3-8='
}
params_str = urllib.parse.urlencode(search)
# print(params_str)
a_bogus = execjs.compile(open('douyin.js').read()).call('get_a_bogus', params_str)
search['a_bogus'] = a_bogus
# response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', params=params, headers=headers)

response = requests.get('https://www.douyin.com/aweme/v1/web/general/search/single/', params=search,
                        headers=search_headers)
pprint.pprint(response.json())
# print(response.json())
