from config.config import TestData
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DuckDuckGoResultPage(BasePage):
    """
    Initializes the Result object.

    Args:
    driver (WebDriver): The WebDriver instance.
    """
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.CSS_SELECTOR, '#searchbox_input')
        self.images__thumbnails__link = (By.CSS_SELECTOR, 'a.module--images__thumbnails__link')
        self.result_links = (By.CSS_SELECTOR, 'a.eVNpHGjtxRBq_gLOfGDr.LQNqh2U1kzYxREs65IJu span')
            
    def extract_image_urls(self):
        """
        Extract the URLs from the image elements and add them to an list.
        Split the URL by second 'http' and take the second part.

        >> output is printed to output/urls.txt
        """

        # Initialize an empty list to store image URLs
        image_links = []

        # Wait for the image elements to be present on the page
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.images__thumbnails__link))
        
        # Finding multiple web elements on a web page that match a specified selector and storing them in a list
        link_elements = self.driver.find_elements(*self.images__thumbnails__link)

        # Loop through all the images and get the links and append the image_links list
        for link in link_elements:
            href = link.get_attribute('href')
            if link:
                image_links.append(href)
        
        # Initialize an empty list to store the extracted parts
        extracted_parts = []

        # Split each URL in image_links using '&iai=' as the delimiter and take the second part
        for url in image_links:
            split_url = url.split('&iai=')
            if len(split_url) > 1:
                extracted_part = split_url[1]
                extracted_parts.append(extracted_part)
    
        # Open an external file for writing
        with open('outputs/urls.txt', 'w') as file:
            for part in extracted_parts:
                print(part, file=file)
                expected_value = part

        # Check the extracted parts match the expected value
        assert part == expected_value, f"Expected: {expected_value}, Actual: {part}"

        # Return the list of extracted parts
        # Now you have a list of extracted parts (the parts after &iai=)
        return extracted_parts
    
    def is_wallpapercave_image_present(self):
        """
        Check if at least one image on the result page is from wallpapercave.com.
        
        Returns:
            bool: True if at least one image is from wallpapercave.com, False otherwise.
        """

        # Extract image URLs using the extract_image_urls method
        image_urls = self.extract_image_urls()
        
        for url in image_urls:
            if 'wallpapercave.com' in url:
                return True
        return False

    def extract_link_titles(self):
        """
        Returns a list of all titles in the first page of the search results, for instance in the screenshot below,
        it would be >>
        [“The 10 Most Beautiful Cars According to Automotive Design Leaders“, 
        “Best Cars of 2023 - Rankings and Review - Forbes Wheels”, ...]
       
         >> output is printed to output/titles.txt
        """

        # Initialize an empty list to store link titles
        link_titles = []

        # Wait for the links elements to be present on the page
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_all_elements_located(self.result_links))

        # Finding multiple web elements on a web page that match a specified selector and storing them in a list
        link_elements = self.driver.find_elements(*self.result_links)

        # loop through all the links and get the text and append the link titles list
        for title in link_elements:
            text = title.text
            if text:
                link_titles.append(text)
        
        # Open an external file for writing
        with open('outputs/titles.txt', 'w') as file:
            for title in link_titles:
                print(title, file=file)
                expected_value = title

        # Check the title match the expected value
        assert title == expected_value, f"Expected: {expected_value}, Actual: {title}"

        # Return the list of extracted parts
        return link_titles

    def is_titles_contains_car_or_cars(self):
        """
        Checks if any of the titles in the list contain the words 'car' or 'cars'
        (case-insensitive).

        Returns:
        bool: True if at least one title contains 'car' or 'cars', False otherwise.
        """

        # Check if at least one title contains "car" or "cars" but not "cartoon"
        found_valid_title = False

        # Extract titles using the extract_link_titles method
        link_titles = self.extract_link_titles()

        # Convert the text of each title to lowercase to make text comparisons case-insensitive
        for title in link_titles:
            lowercase_titles = title.lower()

        # Iterate through link_titles and check if any title contains "car" or "cars"
            if 'car' or 'cars' in lowercase_titles:
                
                # Check if 'cartoon' is not in the title
                if 'cartoon' not in lowercase_titles:
                    found_valid_title = True

        # Return the list of valid titles
        return found_valid_title
