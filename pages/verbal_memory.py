import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class VerbalMemory:

    def __init__(self, driver):
        self.driver = driver
        self.wordList = []

    def get_new_word(self):
        wordEl = self.driver.find_element(By.CLASS_NAME, "word")
        return wordEl.text

    def is_word_in_list(self, word):
        if word in self.wordList:
            return True
        else:
            return False

    def next_question(self):
        pass

    def solve_question(self):
        new_word = self.get_new_word()
        if self.is_word_in_list(new_word):
            seen_button = self.driver.find_elements(By.CLASS_NAME, 'e19owgy710')[0]
            seen_button.click()
        else:
            new_button = self.driver.find_elements(By.CLASS_NAME, 'e19owgy710')[1]
            new_button.click()
            self.wordList.append(new_word)

    def finish(self):
        time.sleep(0.1)
        seen_button = self.driver.find_elements(By.CLASS_NAME, 'e19owgy710')[0]
        seen_button.click()

        try:
            if seen_button.text == "SEEN":
                self.finish()
        except:
            save_button = self.driver.find_elements(By.CLASS_NAME, 'e19owgy710')[0]
            save_button.click()

    def start(self):
        self.driver.get("https://humanbenchmark.com/tests/verbal-memory")

        time.sleep(1)

        startbtn = self.driver.find_element(By.CLASS_NAME, 'e19owgy710')
        startbtn.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "word"))
        )

        for i in range(500):
            self.solve_question()

        self.finish()
