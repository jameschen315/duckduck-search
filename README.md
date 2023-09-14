# Selenium Resources

https://selenium-python.readthedocs.io/index.html - This is not an official documentation. 


1) Download browser specific drivers:
Chrome: https://chromedriver.chromium.org/downloads
Firefox: https://github.com/mozilla/geckodriver/releases

2) Setup selenium webdriver
pip install selenium - selenium 3.0x
pip install selenium4x
or through Pycharm project settings...

3) To run the test, in the main folder, type this command: pytest tests/test_search.py

4) To run individual, from the main folder, type this command: pytest -k test_titles_contains_car_or_cars