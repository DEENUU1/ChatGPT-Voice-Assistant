import unittest
from unittest.mock import MagicMock, patch

from welcome import Welcome


class TestNews(unittest.TestCase):
    """ Test Cases for Welcome class methods """

    @patch('welcome.Welcome._get_current_time')
    def test_get_current_time_success(self, mock_data):
        mock_data.return_value = "17:20"
        result = Welcome._get_current_time()
        self.assertEqual(result, "17:20")

    @patch('welcome.Welcome._get_current_time')
    def test_get_current_time_failed(self, mock_data):
        mock_data.return_value = "17:20"
        result = Welcome._get_current_time()
        self.assertNotEqual(result, 17)

    @patch('welcome.Welcome._get_current_data')
    def test_get_current_date_success(self, mock_data):
        mock_data.return_value = "Monday"
        result = Welcome._get_current_data()
        self.assertEqual(result, "Monday")

    @patch('welcome.Welcome._get_current_data')
    def test_get_current_date_failed(self, mock_data):
        mock_data.return_value = 1
        result = Welcome._get_current_data()
        self.assertNotEqual(result, "Monday")

    @patch('welcome.Welcome._get_current_time')
    @patch('welcome.Welcome._get_current_data')
    def test_return_welcome_message(self, mock_time, mock_data,):
        mock_time.return_value = "17:20"
        mock_data.return_value = "Monday"
        result = Welcome().return_welcome_message('Kacper')
        expected = "Welcome Kacper today is 17:20 Monday. " \
                   "You are about to hear today's news release. " \
                   "Have a good day and see you later! "
        self.assertEqual(result, expected)
