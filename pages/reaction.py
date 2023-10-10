import time

from selenium.webdriver.common.by import By


class Reaction:
    def __init__(self, driver):
        self.driver = driver
        self.box = None
        self.count = 0

    def start(self):
        self.driver.get("https://humanbenchmark.com/tests/reactiontime")

        time.sleep(1)

        self.box = self.driver.find_element(By.CLASS_NAME, 'e18o0sx0')
        self.box.click()

        self.get_color()

    def save(self):
        time.sleep(1)
        btn = self.driver.find_element(By.CLASS_NAME, "e19owgy710")
        btn.click()

    def click(self):
        self.box.click()
        self.count += 1

        if self.count >= 5:
            self.save()
        else:
            self.get_color()

    def get_color(self):
        bgValue = self.box.value_of_css_property('background-color')

        if bgValue == "rgba(43, 135, 209, 1)":
            self.box.click()

        while not bgValue == "rgba(75, 219, 106, 1)":
            bgValue = self.box.value_of_css_property('background-color')

        self.click()
