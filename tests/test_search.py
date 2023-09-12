import pytest
import time
from builtins import AssertionError
from config.config import TestData
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


# Define a pytest fixture for WebDriver setup
@pytest.fixture(scope="function")
def driver():

    # Initialize WebDriver
    chrome_service = ChromeService(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    driver = webdriver.Chrome(service=chrome_service)
    driver.get(TestData.BASE_URL)    

    # Provide the WebDriver to the tests
    yield driver

    # Teardown: Close the WebDriver after all tests are done
    driver.quit()

# Use the driver fixture in your test class
@pytest.mark.usefixtures("driver")
class TestDuckDuckGoSearch:

    def test_duckduckgo_url(self, driver):
        """
        Check user is on DuckDuckGo webpage.
        """

        # Create objects of page classes using the initialized driver
        search_page = DuckDuckGoSearchPage(driver)

        current_url = driver.current_url
        expected_url = TestData.BASE_URL
        assert current_url == expected_url, f"Current URL is {current_url}, not {expected_url}"
    
    def test_image_urls_from_images(self, driver):
        """
        Test URLs from images section and stripped duckduckgo URL part. 
        >> 
        return http://wallpapercave.com/wp/Aw8HGgD.jpg&atb=v349-1 for this URL.
        >> print to external file
        with open('outputs/urls.txt', 'w') as file:
            for part in extracted_parts:
                print(part, file=file)
                expected_value = part
        Test the urls match the expected value.
        """

        # Create objects of page classes using the initialized driver
        result_page = DuckDuckGoResultPage(driver)
        search_page = DuckDuckGoSearchPage(driver)
        
        search_page.search(TestData.SEARCH_PHASE)

        # Call the method to extract image URLs
        result_page.extract_image_urls()

    def test_links_titles(self, driver):
        """
        Test all titles from links in page 1 search result. 
        Print to external file >>
         with open('outputs/titles.txt', 'w') as file:
            for title in link_titles:
                print(title, file=file)
                expected_value = title
        Test the title match the expected value
        """

        # Create objects of page classes using the initialized driver
        result_page = DuckDuckGoResultPage(driver)
        search_page = DuckDuckGoSearchPage(driver)
        
        search_page.search(TestData.SEARCH_PHASE)

        # Call the method to extract image URLs
        result_page.extract_link_titles()
        
    def test_wallpapercave_image_present(self, driver):
        """
        Test images contain wallpapercave.com. 
        """

        # Create objects of page classes using the initialized driver
        result_page = DuckDuckGoResultPage(driver)
        search_page = DuckDuckGoSearchPage(driver)
        
        search_page.search(TestData.SEARCH_PHASE)

        is_wallpapercave_image_present = result_page.is_wallpapercave_image_present()

        time.sleep(2)

        # If no image from "wallpapercave.com" is found, capture a screenshot
        if not is_wallpapercave_image_present:
            driver.get_screenshot_as_file("outputs/no_wallpapercave_images.png")
        
        # Check if at least one image is from "wallpapercave.com"
        assert is_wallpapercave_image_present, "No image from wallpapercave.com found on the result page"

    def test_titles_contains_car_or_cars(self, driver):
        """
        Test titles contains car or cars and not cartoon
        """

        # Create objects of page classes using the initialized driver
        result_page = DuckDuckGoResultPage(driver)
        search_page = DuckDuckGoSearchPage(driver)
        
        search_page.search(TestData.SEARCH_PHASE)

        is_titles_contains_car_or_cars = result_page.is_titles_contains_car_or_cars()
        
        time.sleep(2)

        try:
            # Check that at least one title contains "car" or "cars" or "cartoon"
            assert is_titles_contains_car_or_cars, "No title contains 'car' or 'cars' or contain 'cartoon'"
        
        except AssertionError:

            # If no 'car' or 'cars' or 'cartoon' presents in title, capture a screenshot
            if not is_titles_contains_car_or_cars:
                driver.get_screenshot_as_file("outputs/no_car_or_cars.png")

                # Re-raise the AssertionError to signal the test failure
                raise  
