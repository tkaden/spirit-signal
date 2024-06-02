import unittest
from unittest.mock import patch, MagicMock
from scraper import setup_driver, change_zip_code, search_spirit, check_availability, scrape_spirits
import pandas as pd

class TestScraper(unittest.TestCase):

    @patch('scraper.webdriver.Chrome')
    def test_setup_driver(self, MockWebDriver):
        driver = setup_driver()
        MockWebDriver.assert_called_once()
        self.assertIsNotNone(driver)

    @patch('scraper.webdriver.Chrome')
    def test_change_zip_code(self, MockWebDriver):
        mock_driver = MockWebDriver()
        mock_driver.find_element.return_value = MagicMock()
        change_zip_code(mock_driver, '90210')
        mock_driver.find_element.assert_called()

    @patch('scraper.webdriver.Chrome')
    def test_search_spirit(self, MockWebDriver):
        mock_driver = MockWebDriver()
        mock_driver.find_element.return_value = MagicMock()
        mock_driver.find_elements.return_value = [MagicMock(text='Vodka')]
        results = search_spirit(mock_driver, 'Vodka')
        self.assertEqual(len(results), 1)

    def test_check_availability(self):
        mock_driver = MagicMock()
        mock_results = [MagicMock(text='Vodka - Available'), MagicMock(text='Whiskey - Out of Stock')]
        available_spirits = check_availability(mock_driver, mock_results)
        self.assertEqual(available_spirits, ['Vodka - Available'])

    @patch('scraper.setup_driver')
    @patch('scraper.change_zip_code')
    @patch('scraper.search_spirit')
    @patch('scraper.check_availability')
    def test_scrape_spirits(self, mock_check_availability, mock_search_spirit, mock_change_zip_code, mock_setup_driver):
        mock_driver = MagicMock()
        mock_setup_driver.return_value = mock_driver
        mock_search_spirit.return_value = [MagicMock(text='Vodka')]
        mock_check_availability.return_value = ['Vodka - Available']
        
        spirits_data = pd.DataFrame({
            "spirit": ["Vodka"],
            "email": ["test@example.com"],
            "zipcode": ["90210"]
        })

        available_spirits = scrape_spirits(spirits_data)
        self.assertEqual(available_spirits, {'test@example.com': ['Vodka - Available']})

if __name__ == "__main__":
    unittest.main()
