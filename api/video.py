from . import api
from flask import jsonify, request
from utils.request import Request

request_instance = Request()  # 创建 Request 类的实例
"""
@desc: 获取视频详细信息
@url: /aweme/v1/web/aweme/detail
@param: aweme_id
"""


@api.route('/aweme/detail/')
def get_detail():
    aweme_id = request.args.get('aweme_id')
    if not aweme_id:
        return jsonify({'error': 'Missing aweme_id parameter'}), 400
    params = {"aweme_id": aweme_id}
    url = '/aweme/v1/web/aweme/detail/'
    aweme_detail = request_instance.getJSON(url, params)  # 直接调用 getJSON 方法
    if aweme_detail:
        return jsonify(aweme_detail)
    else:
        api.logger.error('Failed to retrieve aweme detail for aweme_id: %s', aweme_id)
        return jsonify({'error': 'Failed to retrieve aweme detail; Check you Cookie!'}), 404


"""
@desc: 获取相关视频
@url：/aweme/related
@param: aweme_id
@param: count
@param: filterGids 第一次可以不传值，第二次传入 第一次请求的aweme_id ;
示例：filterGids: 7380308118061780287,7386945509082025225,
7386952050208247080,7379532523379903795,7379995831534947618,7360577857900350746,7391047134314908982,
7391866100910247207,7405446866906729782
@param： refresh_index  第一次：1 
"""


@api.route('/aweme/related/')
def get_related():
    aweme_id = request.args.get('aweme_id')
    count = request.args.get('count')
    filter_gids = request.args.get('filterGids')
    refresh_index = request.args.get('refresh_index')
    if not aweme_id:
        return jsonify({'error': 'Missing aweme_id parameter'}), 400
    params = {"aweme_id": aweme_id, "count": count, "filterGids": filter_gids,
              "awemePcRecRawData": '{"is_client":false}', "sub_channel_id": 0, "Seo-Flag": 0,
              "refresh_index": refresh_index
              }
    url = '/aweme/v1/web/aweme/related/'
    aweme_list = request_instance.getJSON(url, params)
    if aweme_list:
        return jsonify(aweme_list)


"""
@desc: 获取视频评论
@url: /aweme/v1/web/comment/list/
@param: cursor 0 第二次请求为上一个请求的请求count；第一次为0 5 第二次为5 20 第三次为25 25依次递增
@param: count 5
"""


@api.route('/comment/list/')
def get_comment_list():
    aweme_id = request.args.get('aweme_id')
    cursor = request.args.get('cursor')
    count = request.args.get('count')
    params = {
        "aweme_id": aweme_id,
        "cursor": cursor,
        "count": count
    }
    url = '/aweme/v1/web/comment/list/'
    comment_list = request_instance.getJSON(url, params)
    if comment_list:
        return jsonify(comment_list)
    else:
        api.logger.error('Failed to retrieve comment list for aweme_id: %s url: %s', aweme_id, url)
        return jsonify({'error': 'Failed to retrieve comment list; Check you Cookie!'}), 404


"""
@desc： 展开更多评论
@url： /aweme/v1/web/comment/list/reply/
@param: item_id 视频id
@param：comment_id 评论id
@param：cursor 0 3 13
@param： count 3 10 10
"""


@api.route('/comment/list/reply/')
def get_reply_list():
    item_id = request.args.get('item_id')  # 视频id
    comment_id = request.args.get('comment_id')
    cursor = request.args.get('cursor')
    count = request.args.get('count')
    params = {
        "item_id": item_id,
        "comment_id": comment_id,
        "cursor": cursor,
        "count": count
    }
    url = '/aweme/v1/web/comment/list/reply/'
    comment_list = request_instance.getJSON(url, params)
    if comment_list:
        return jsonify(comment_list)
    else:
        api.logger.error('Failed to retrieve comment list for aweme_id: %s url: %s', item_id, url)
        return jsonify({'error': 'Failed to retrieve comment list; Check you Cookie!'}), 404
