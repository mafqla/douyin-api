import unittest
from pprint import pprint

from app import app


class TestLiveCase(unittest.TestCase):
    # 初始化测试客户端
    def setUp(self):
        self.client = app.test_client()

    # 测试/web/webcast/room/info_by_scene/
    def test_get_live_info(self):
        res = self.client.get('/aweme/v1/web/webcast/room/info_by_scene/?room_id=7418107379843173154')
        self.assertEqual(res.status_code, 200)
        print('live_info value:')
        pprint(res.get_json())


if __name__ == '__main__':
    unittest.main()
