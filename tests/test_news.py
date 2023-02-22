import os
import json
from unittest import TestCase, mock
from news import News
import pytest

class MockResponse:
    """Mock class for Response"""

    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code

class TestNews(TestCase):
    """Test case for News class"""

    @mock.patch.dict({'NEWS_KEY': 'test_api_key'})
    @mock.patch('news.get')
    def test_get_news_url_success(self, mock_get):
        mock_response = MockResponse(
            json.dumps({
                'status': 'ok',
                'articles': [
                    {'url': 'https://testurl1.com'},
                    {'url': 'https://testurl2.com'}
                ]
            }), 200)
        mock_get.return_value = mock_response
        news = News()
        urls = news.get_news_urls()

        assert urls == ['https://testurl1.com','https://testurl2.com']


    @mock.patch.dict({'NEWS_KEY': 'test_api_key'})
    @mock.patch('news.get')
    def test_get_news_url_failled(self, mock_get):
        mock_response = MockResponse(
                json.dumps({
                    'status': 'error',
                    'message': 'Invalid API key'
                }), 401)
        mock_get.return_value = mock_response
        news = News()

        with pytest.raises(Exception):
            news.get_news_urls()