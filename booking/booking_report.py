# This file is going to include methods that will parse
# the specific data we need from each of the deal boxes
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self, boxes):
        self.boxes = boxes

    def pull_attributes(self):
        collection = []
        for box in self.boxes:
            name = box.find_element(By.CSS_SELECTOR, '[data-testid="title"]').text.strip()

            price = box.find_element(By.CSS_SELECTOR, '[data-testid="price-and-discounted-price"]').text.strip()

            score = box.find_element(By.CSS_SELECTOR, '[data-testid="review-score"]').text.strip()

            collection.append([name, price, score])
        return collection

    
