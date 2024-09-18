from . import api
from utils.request import Request
from flask import request, jsonify

request_instance = Request()  # 创建 Request 类的实例

'''
@desc: 搜索
@url: /aweme/v1/web/general/search/single/
@param: keyword 关键词
@param: offset 游标
@param: count 默认 15
@param： filter_selected  {
  /**
   * 指定排序方式。
   * 0 - 综合排序
   * 1 - 最新发布
   * 3 - 最多点赞
   */
  sort_type?: 0 | 1 | 3

  /**
   * 指定发布时间的范围。
   * 0 - 不限
   * 1 - 一天内
   * 7 - 一周内
   * 180 - 半年内
   */
  public_time?: 0 | 1 | 7 | 180

  /**
   * 指定视频时长的筛选条件。
   * "" - 不限
   * "0-1" - 1分钟以下
   * "1-5" - 1-5分钟
   * "5-10000" - 5分钟以上
   */
  filter_duration?: '' | '0-1' | '1-5' | '5-10000'

  /**
   * 指定搜索范围。
   * "0" - 不限
   * "3" - 关注的人
   * "1" - 最近看过
   * "2" - 还未看过
   */
  search_range?: '0' | '3' | '1' | '2'

  /**
   * 指定内容类型。
   * "0" - 不限
   * "1" - 视频
   * "2" - 图文
   */
  content_type?: '0' | '1' | '2'
}
@param: is_filter_search = 1 | 0
@param: list_type= single | multi
'''


@api.route('/general/search/single/')
def get_search():
    keyword = request.args.get('keyword')
    offset = request.args.get('offset')
    count = request.args.get('count')
    filter_selected = request.args.get('filter_selected')
    is_filter_search = request.args.get('is_filter_search'),
    list_type = request.args.get('list_type')
    url = '/aweme/v1/web/general/search/single/'
    params = {
        'search_channel': 'aweme_general',
        'enable_history': 'enable_history',
        'keyword': keyword,
        'query_correct_type': '1',
        'offset': offset,
        'count': count,
        'need_filter_settings': 'need_filter_settings',
        'list_type': list_type
    }
    if is_filter_search == 1:
        params['filter_selected'] = filter_selected

    print(params)
    search_data = request_instance.getJSON(url, params)
    if search_data:
        return jsonify(search_data)
    else:
        return jsonify({'error': 'Failed to retrieve search_data; Check you Cookie and Referer!'}), 403
