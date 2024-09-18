import unittest
from pprint import pprint

from app import app
from json import dumps


class TestSearchAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.keyword = "赵露思"  # Assuming 'test' is the keyword for all tests
        self.offset = 0
        self.count = 15

    def test_search_with_is_filter_search(self):
        # Test with is_filter_search parameter
        filter_selected = dumps({
            "sort_type": 1,
            "public_time": 7,
            "filter_duration": "1-5",
            "search_range": "3",
            "content_type": "1"
        })

        response = self.app.get(
            f'/aweme/v1/web/general/search/single/?keyword={self.keyword}&offset={self.offset}&count={self.count}&is_filter_search=1&filter_selected={filter_selected}')
        self.assertEqual(response.status_code, 200)
        print('Is Filter Search Result:')
        pprint(response.get_json())

    def test_search_with_list_type(self):
        # Test with list_type parameter
        response = self.app.get(
            f'/aweme/v1/web/general/search/single/?keyword={self.keyword}&offset={self.offset}&count={self.count}&is_filter_search=0&list_type=multi')
        self.assertEqual(response.status_code, 200)
        print('List Type Search Result:')
        pprint(response.get_json())

    def test_search_with_all_parameters(self):
        # Test with all three parameters together
        filter_selected = dumps({
            "sort_type": 3,
            "public_time": 180,
            "filter_duration": "5-10000",
            "search_range": "1",
            "content_type": "2"
        })
        response = self.app.get(
            f'/aweme/v1/web/general/search/single/?keyword={self.keyword}&offset={self.offset}&count={self.count}&filter_selected={filter_selected}&is_filter_search=1&list_type=single')
        self.assertEqual(response.status_code, 200)
        print('Search Result with All Parameters:')
        pprint(response.get_json())


if __name__ == '__main__':
    unittest.main()
