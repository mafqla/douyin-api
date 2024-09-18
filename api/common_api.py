from . import api
from utils.request import Request
from flask import request, jsonify

request_instance = Request()  # 创建 Request 类的实例

'''
@desc: 底部栏推荐词
@url: aweme/v1/web/seo/inner/link/
'''


@api.route('/seo/inner/link/')
def get_seo_link():
    url = '/aweme/v1/web/seo/inner/link/'
    params = {
        'channel': 'channel_pc_web'
    }
    seo_link = request_instance.getJSON(url, params)
    if seo_link:
        return jsonify(seo_link)
    else:
        return jsonify({'error': 'Failed to retrieve seo_link; Check you Cookie and Referer!'}), 403


'''
@desc: 获取表情列表
@url： '/aweme/v1/web/emoji/list'
'''


@api.route('/emoji/list/')
def get_emoji_list():
    url = '/aweme/v1/web/emoji/list'
    params = {
        'channel': 'channel_pc_web'
    }
    emoji_list = request_instance.getJSON(url, params)
    if emoji_list:
        return jsonify(emoji_list)
    else:
        return jsonify({'error': 'Failed to retrieve emoji_list; Check you Cookie and Referer!'}), 403


'''
@desc: 自定义的表情或者收藏的
@url: /aweme/v1/web/im/resources/emoticon/trending
'''


@api.route('/im/resources/emoticon/trending')
def get_emoticon_list():
    url = '/aweme/v1/web/im/resources/emoticon/trending'
    cursor = request.args.get('cursor')
    count = request.args.get('count')
    params = {
        'cursor': cursor,
        'count': count
    }
    emoticon_list = request_instance.getJSON(url, params)
    if emoticon_list:
        return jsonify(emoticon_list)
    else:
        return jsonify({'error': 'Failed to retrieve emoticon_list; Check you Cookie and Referer!'}), 403


'''
@desc: 搜索框热搜列表
@url: /aweme/v1/web/hot/search/list/
'''


@api.route('hot/search/list/')
def get_hot_list():
    url = '/aweme/v1/web/hot/search/list/'
    cursor = request.args.get('cursor')
    count = request.args.get('count')
    params = {
    }
    hot_list = request_instance.getJSON(url, params)
    if hot_list:
        return jsonify(hot_list)
    else:
        return jsonify({'error': 'Failed to retrieve emoticon_list; Check you Cookie and Referer!'}), 403
