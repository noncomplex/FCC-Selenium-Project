#This file will include a class with instance methods.
# That will be responsible to interact with our website
# After we have some results, to apply filtrations.
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltrations:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, '[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-selected-sorter="popularity"]'
        )
        element.click()
        sort_lowest_button = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[data-id="price"]'
        )
        sort_lowest_button.click()