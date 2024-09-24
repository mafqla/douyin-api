from . import api
from utils.request import Request
from flask import request, jsonify

request_instance = Request()  # 创建 Request 类的实例
'''
@desc: 获取用户个人的信息
@url: '/aweme/v1/web/user/profile/self/'
'''


@api.route('/user/profile/self/')
def get_user_info_self():
    url = '/aweme/v1/web/user/profile/self/'
    params = {

    }
    user_info = request_instance.getJSON(url, params)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({'error': 'Failed to retrieve userinfo; Check you Cookie and Referer!'}), 403


"""
@desc: 获取其他用户信息
@url: /aweme/v1/web/user/profile/other/
"""


@api.route('/user/profile/other/')
def get_user_info():
    sec_user_id = request.args.get('sec_user_id')
    url = '/aweme/v1/web/user/profile/other/'
    params = {
        'sec_user_id': sec_user_id,
        'source': 'channel_pc_web',
        'publish_video_strategy_type': '2',
        'personal_center_strategy': '1'
    }
    user_info = request_instance.getJSON(url, params)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({'error': 'Failed to retrieve userinfo; Check you Cookie and Referer!'}), 403


"""
@desc: 获取用户作品列表
@url：/aweme/v1/web/aweme/post/
@param: forward_end_cursor 上一个接口的max_cursor 
@param: max_cursor
"""


@api.route('/aweme/post/')
def get_user_post():
    sec_user_id = request.args.get('sec_user_id')
    count = request.args.get('count')
    max_cursor = request.args.get('max_cursor')
    url = '/aweme/v1/web/aweme/post/'
    params = {
        'sec_user_id': sec_user_id,
        'count': count,
        'max_cursor': max_cursor,
        'locate_query': 'false',
        'show_live_replay_strategy': '1',
        'need_time_list': '1',
        'time_list_query': '0',
        'publish_video_strategy_type': '2'
    }
    post_list = request_instance.getJSON(url, params)
    if post_list:
        return jsonify(post_list)
    else:
        return jsonify({'error': 'Failed to retrieve post_list; Check you Cookie and Referer!'}), 404


"""
@desc: 获取用户喜欢的列表
@url: /aweme/v1/web/aweme/favorite/
"""


@api.route('/aweme/favorite/')
def get_user_favorite():
    sec_user_id = request.args.get('sec_user_id')
    count = request.args.get('count')
    min_cursor = request.args.get('min_cursor')
    max_cursor = request.args.get('max_cursor')
    url = '/aweme/v1/web/aweme/favorite/'
    params = {
        'sec_user_id': sec_user_id,
        'count': count,
        'max_cursor': max_cursor,
        'min_cursor': min_cursor,
        'publish_video_strategy_type': '2'
    }
    favorite_list = request_instance.getJSON(url, params)
    if favorite_list:
        return jsonify(favorite_list)
    else:
        return jsonify({'error': 'Failed to retrieve favorite_list; Check you Cookie and Referer!'}), 404


"""
@desc: 获取用户收藏列表
@url： /aweme/v1/web/aweme/listcollection/
"""


@api.route('/aweme/listcollection/')
def get_list_collection():
    count = request.args.get('count')
    cursor = request.args.get('cursor')

    url = '/aweme/v1/web/aweme/listcollection/'
    params = {

    }
    data = {
        'count': count,
        'cursor': cursor
    }
    collection_list = request_instance.getJSON(url, params, data)
    if collection_list:
        return jsonify(collection_list)
    else:
        return jsonify({'error': 'Failed to retrieve  collection_list; Check you Cookie and Referer!'}), 404


"""
@desc: 收藏的音乐
@url: /aweme/v1/web/music/listcollection/
@param: cursor 0
@param: count 18
"""


@api.route('/music/listcollection/')
def get_list_collection_music():
    count = request.args.get('count')
    cursor = request.args.get('cursor')

    url = '/aweme/v1/web/music/listcollection/'
    params = {
        'count': count,
        'cursor': cursor
    }
    music_list = request_instance.getJSON(url, params)
    if music_list:
        return jsonify(music_list)
    else:
        return jsonify({'error': 'Failed to retrieve  music_list; Check you Cookie and Referer!'}), 404


"""
@desc: 收藏夹
@url: /aweme/v1/web/collects/list/
@param: cursor 0
@param: count 18
"""


@api.route('/collects/list/')
def get_list_collects():
    count = request.args.get('count')
    cursor = request.args.get('cursor')

    url = '/aweme/v1/web/collects/list/'
    params = {
        'count': count,
        'cursor': cursor
    }
    collects_list = request_instance.getJSON(url, params)
    if collects_list:
        return jsonify(collects_list)
    else:
        return jsonify({'error': 'Failed to retrieve  collects_list; Check you Cookie and Referer!'}), 404


"""
@desc: 收藏夹视频信息
@url: /aweme/v1/web/collects/video/list/
@param: cursor 0
@param: count 18
"""


@api.route('/collects/video/list/')
def get_list_collects_video():
    collects_id = request.args.get('collects_id')
    count = request.args.get('count')
    cursor = request.args.get('cursor')

    url = '/aweme/v1/web/collects/video/list/'
    params = {
        'collects_id': collects_id,
        'count': count,
        'cursor': cursor
    }
    collects_video_list = request_instance.getJSON(url, params)
    if collects_video_list:
        return jsonify(collects_video_list)
    else:
        return jsonify({'error': 'Failed to retrieve  collects_video_list; Check you Cookie and Referer!'}), 404


"""
@desc: 收藏的合集
@url: /aweme/v1/web/mix/listcollection/
"""


@api.route('/mix/listcollection/')
def get_list_collection_mix():
    count = request.args.get('count')
    cursor = request.args.get('cursor')

    url = '/aweme/v1/web/mix/listcollection/'
    params = {
        'count': count,
        'cursor': cursor
    }
    mix_list = request_instance.getJSON(url, params)
    if mix_list:
        return jsonify(mix_list)
    else:
        return jsonify({'error': 'Failed to retrieve  mix_list; Check you Cookie and Referer!'}), 404


"""
@desc: 收藏的短剧
@url: /aweme/v1/web/series/collections
"""


@api.route('/series/collections/')
def get_list_collection_series():
    count = request.args.get('count')
    cursor = request.args.get('cursor')

    url = '/aweme/v1/web/series/collections'
    params = {
        'count': count,
        'cursor': cursor
    }
    series_list = request_instance.getJSON(url, params)
    if series_list:
        return jsonify(series_list)
    else:
        return jsonify({'error': 'Failed to retrieve  series_list; Check you Cookie and Referer!'}), 404


"""
@desc: 用户创建的合集
@url: /aweme/v1/web/mix/list/
"""


@api.route('/mix/list/')
def get_mix_list():
    sec_user_id = request.args.get('sec_user_id')
    count = request.args.get('count')
    cursor = request.args.get('cursor')

    url = '/aweme/v1/web/mix/list/'
    params = {
        'sec_user_id': sec_user_id,
        'count': count,
        'cursor': cursor,
        'req_from': 'channel_pc_web'
    }
    mix_list = request_instance.getJSON(url, params)
    if mix_list:
        return jsonify(mix_list)
    else:
        return jsonify({'error': 'Failed to retrieve  mix_list; Check you Cookie and Referer!'}), 404


"""
@desc: 获取用户观看历史列表
@url: /aweme/v1/web/history/read/
"""


@api.route('/history/read/')
def get_history_read():
    count = request.args.get('count')
    cursor = request.args.get('cursor')

    url = '/aweme/v1/web/history/read/'
    params = {
        'count': count,
        'cursor': cursor
    }
    history_read = request_instance.getJSON(url, params)
    if history_read:
        return jsonify(history_read)
    else:
        return jsonify({'error': 'Failed to retrieve  history_read; Check you Cookie and Referer!'}), 404


"""
@desc: 获取用户关系列表
@url：/aweme/v1/web/im/spotlight/relation/
"""


@api.route('/im/spotlight/relation/')
def get_relation():
    count = request.args.get('count')
    min_time = request.args.get('min_time')
    max_time = request.args.get('max_time')  # 当前的时间戳
    url = '/aweme/v1/web/im/spotlight/relation/'
    params = {
        'count': count,
        'max_time': max_time,
        'min_time': min_time,
        'need_remove_share_panel': 'true',
        'need_sorted_info': 'true',
        'with_fstatus': '1'
    }
    relation = request_instance.getJSON(url, params)
    if relation:
        return jsonify(relation)
    else:
        return jsonify({'error': 'Failed to retrieve relation; Check you Cookie and Referer!'}), 404


"""
@desc: 获取用户关注列表
@url: /aweme/v1/web/user/following/list/
@param: source_type 1最近关注 3最早关注 4 综合排序
"""


@api.route('/user/following/list/')
def get_user_following():
    user_id = request.args.get('user_id')
    sec_user_id = request.args.get('sec_user_id')
    count = request.args.get('count')
    source_type = request.args.get('source_type')
    offset = request.args.get('offset')
    min_time = request.args.get('min_time')
    max_time = request.args.get('max_time')
    url = '/aweme/v1/web/user/following/list/'
    params = {
        'user_id': user_id,
        'sec_user_id': sec_user_id,
        'count': count,
        'offset': offset,
        'max_time': max_time,
        'min_time': min_time,
        'source_type': source_type,
        'gps_access': '0',
        'address_book_access': '0',
        'is_top': '1',
    }
    following_list = request_instance.getJSON(url, params)
    if following_list:
        return jsonify(following_list)
    else:
        return jsonify({'error': 'Failed to retrieve following_list; Check you Cookie and Referer!'}), 404


"""
@desc: 获取粉丝列表
@url: /aweme/v1/web/user/follower/list/
"""


@api.route('/user/follower/list/')
def get_user_follower():
    user_id = request.args.get('user_id')
    sec_user_id = request.args.get('sec_user_id')
    count = request.args.get('count')
    source_type = request.args.get('source_type')
    offset = request.args.get('offset')
    min_time = request.args.get('min_time')
    max_time = request.args.get('max_time')
    url = '/aweme/v1/web/user/follower/list/'
    params = {
        'user_id': user_id,
        'sec_user_id': sec_user_id,
        'count': count,
        'offset': offset,
        'max_time': max_time,
        'min_time': min_time,
        'source_type': source_type,
        'gps_access': '0',
        'address_book_access': '0',
        'is_top': '1',
    }
    follower_list = request_instance.getJSON(url, params)
    if follower_list:
        return jsonify(follower_list)
    else:
        return jsonify({'error': 'Failed to retrieve follower_list; Check you Cookie and Referer!'}), 404


"""
@desc: 用户主页搜索
@url: /aweme/v1/web/home/search/item/
@param: search_channel= aweme_favorite_video | aweme_collect_video | aweme_viewed_video | aweme_personal_home_video
"""


@api.route('/home/search/item/')
def get_search_item():
    search_channel = request.args.get('search_channel')
    keyword = request.args.get('keyword')
    from_user = request.args.get('from_user')
    count = request.args.get('count')
    offset = request.args.get('offset')
    url = '/aweme/v1/web/home/search/item/'
    params = {
        'search_channel': search_channel,
        'search_source': 'normal_search',
        'from_user': from_user,
        'count': count,
        'offset': offset,
        'search_scene': 'douyin_search',
        'sort_type': '0',
        'publish_time': '0',
        'is_filter_search': '0',
        'query_correct_type': '1',
        'keyword': keyword,
        'search_id': ''
    }
    search_item = request_instance.getJSON(url, params)
    if search_item:
        return jsonify(search_item)
    else:
        return jsonify({'error': 'Failed to retrieve search_item; Check you Cookie and Referer!'}), 404
