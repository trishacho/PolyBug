import unittest
from unittest.mock import patch, MagicMock
from your_module import download_helper

class TestDownloadHelper(unittest.TestCase):
    @patch('your_module.open_file')
    @patch('builtins.input')
    def test_found_title_and_source(self, mock_input, mock_open_file):
        mock_input.side_effect = ['naruto', '1']
        mock_open_file.return_value = [
            {'title': 'Naruto', 'source': 'mangadex'},
            {'title': 'Bleach', 'source': 'mangadex'}
        ]
        result = download_helper('mangadex')
        self.assertEqual(result, 0)

    @patch('your_module.open_file')
    @patch('builtins.input')
    def test_found_title_but_wrong_source(self, mock_input, mock_open_file):
        mock_input.side_effect = ['naruto']
        mock_open_file.return_value = [
            {'title': 'Naruto', 'source': 'mangakakalot'},
        ]
        result = download_helper('mangadex')
        self.assertIsNone(result)

    @patch('your_module.open_file')
    @patch('builtins.input')
    def test_no_title_match(self, mock_input, mock_open_file):
        mock_input.side_effect = ['one piece']
        mock_open_file.return_value = [
            {'title': 'Naruto', 'source': 'mangadex'},
        ]
        result = download_helper('mangadex')
        self.assertEqual(result, -1)

    @patch('your_module.open_file')
    @patch('builtins.input')
    def test_exit_on_zero(self, mock_input, mock_open_file):
        mock_input.side_effect = ['Naruto', '0']
        mock_open_file.return_value = [
            {'title': 'Naruto', 'source': 'mangadex'}
        ]
        result = download_helper('mangadex')
        self.assertIsNone(result)

    @patch('your_module.open_file')
    @patch('builtins.input')
    def test_index_out_of_bounds(self, mock_input, mock_open_file):
        mock_input.side_effect = ['Naruto', '5']
        mock_open_file.return_value = [
            {'title': 'Naruto', 'source': 'mangadex'}
        ]
        result = download_helper('mangadex')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()