import time

from selenium.webdriver.common.by import By


class Aim:
    def __init__(self, driver):
        self.driver = driver
        self.target = None

    def start(self):
        self.driver.get("https://humanbenchmark.com/tests/aim")
        self.target = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]/div/div/div[6]')
        self.target.click()

        self.run()

    def save(self):
        btn = self.driver.find_element(By.CLASS_NAME, "e19owgy710")
        btn.click()

    def run(self):
        for i in range(30):
            self.target = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div/div/div[6]')
            self.target.click()

        self.save()
