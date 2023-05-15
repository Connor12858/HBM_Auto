from selenium.webdriver.common.by import By
import pyautogui


class Typing:
    def __init__(self, driver):
        self.driver = driver

    def get_letters(self):
        letters = self.driver.find_elements(By.CLASS_NAME, "incomplete")
        return letters

    def input_letter(self, letter):
        area = self.driver.find_elements(By.CLASS_NAME, 'e19owgy78')[3]
        pyautogui.write(letter)

    def start(self):
        self.driver.get('https://humanbenchmark.com/tests/typing')

        letters = self.get_letters()
        for i in range(len(letters)):
            self.input_letter(letters[i].text)


