import unittest
import json
from unittest.mock import MagicMock, patch

from news import News


class TestNews(unittest.TestCase):
    """ Test Cases for news class methods """
    def setUp(self) -> None:
        with open('tests/news_fixture.json', encoding='utf-8') as json_file:
            self.fake_news_information = json.load(json_file)
        self.api_key = 'fakeapikey123'

    @patch('news.get')
    def test_get_news(self, mock_get):
        """ Test success get news from the API """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = json.dumps(self.fake_news_information)
        mock_get.return_value = mock_response
        result = News._get_news_urls(self, 'PL')
        self.assertEqual(result, ["https://news.google.com/rss/articles/CBMipwFodHRw"])