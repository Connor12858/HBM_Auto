from selenium.webdriver.common.by import By
import pyautogui
import win32gui


class Typing:
    def __init__(self, driver):
        self.driver = driver

    def get_letters(self):
        print("Do not touch anything\nGetting the paragraph...")
        letters = []
        spans = self.driver.find_elements(By.CLASS_NAME, "incomplete")
        
        for span in spans:
            if span.text != "":
                letters.append(span.text)
            else:
                letters.append(" ")
        
        return letters

    def input_letters(self, letters):
        print("Continue to not touch anything\nTyping...")
        area = self.driver.find_element(By.CLASS_NAME, 'letters')
        area.click()
        
        for letter in letters:
            area.send_keys(letter)
            
        self.save()
            
    def save(self):
        save = self.driver.find_element(By.CLASS_NAME, "e19owgy710")
        save.click()

    def start(self):
        self.driver.get('https://humanbenchmark.com/tests/typing')

        letters = self.get_letters()
        self.input_letters(letters)


