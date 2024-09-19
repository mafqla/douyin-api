import unittest
from pprint import pprint

from app import app


class TestCase(unittest.TestCase):
    # 初始化测试客户端
    def setUp(self):
        self.client = app.test_client()

    # 测试 /aweme/v1/web/seo/inner/link 路由
    def test_get_seo_link(self):
        response = self.client.get('/aweme/v1/web/seo/inner/link/')
        print("SEO Link Response:")  # 打印返回的 JSON 数据
        pprint(response.get_json())
        self.assertEqual(response.status_code, 200)

    # 测试 /aweme/v1/web/emoji/list 路由
    def test_get_emoji_list(self):
        response = self.client.get('/aweme/v1/web/emoji/list/')
        print("Emoji List Response:")  # 打印返回的 JSON 数据
        pprint(response.get_json())
        self.assertEqual(response.status_code, 200)

    # 测试 '/aweme/v1/web/im/resources/emoticon/trending'
    def test_get_emoticon_list(self):
        response = self.client.get('/aweme/v1/web/im/resources/emoticon/trending?cursor=0&count=80')
        print("emoticon List Response:")  # 打印返回的 JSON 数据
        pprint(response.get_json())
        self.assertEqual(response.status_code, 200)

    # 测试/aweme/v1/web/tab/feed/
    def test_get_recommend_list(self):
        response = self.client.get('/aweme/v1/web/tab/feed/?count=10')
        print('Recommend List Res')
        pprint(response.get_json())
        self.assertEqual(response.status_code, 200)

    # 测试/aweme/v1/web/hot/search/list/
    def test_get_hot_list(self):
        res = self.client.get('/aweme/v1/web/hot/search/list/')
        self.assertEqual(res.status_code, 200)
        print('Hot list value:')
        pprint(res.get_json())

    # 测试/aweme/v1/web/api/suggest_words/
    def test_get_suggest_words(self):
        res = self.client.get('/aweme/v1/web/api/suggest_words/?query=雍华盛会警察到九楼后续&count=8')
        self.assertEqual(res.status_code, 200)
        print('suggest_words value:')
        pprint(res.get_json())


if __name__ == '__main__':
    unittest.main()
