import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class NumberMemory:

    def __init__(self, driver):
        self.driver = driver
        self.num = "0"
        self.sleepCount = 3
        self.numCounter = 0
        
    def get_num(self):
        self.num = self.driver.find_element(By.CLASS_NAME, 'big-number').text
        
        time.sleep(self.sleepCount)
        
        self.enter_number()
        
    def continue_number(self):
        nextBtn = self.driver.find_element(By.CLASS_NAME, "e19owgy710")
        nextBtn.click()
        
        self.numCounter += 1
        self.sleepCount += 0.75
        
        self.get_num()
        
    def end(self):
        savebtn = self.driver.find_element(By.CLASS_NAME, "e19owgy710")
        savebtn.click()
    
    def enter_number(self):
        inputNum = self.driver.find_element(By.TAG_NAME, "input")
        inputNum.click()
        if self.numCounter < 20:
            inputNum.send_keys(self.num)
            
            submit = self.driver.find_element(By.CLASS_NAME, "e19owgy710")
            submit.click()
            
            self.continue_number()
        else:
            inputNum.send_keys("0")
            
            submit = self.driver.find_element(By.CLASS_NAME, "e19owgy710")
            submit.click()
            
            time.sleep(1.5)
            
            self.end()
            
        
    def start(self):
        self.driver.get("https://humanbenchmark.com/tests/number-memory")

        time.sleep(1)

        startbtn = self.driver.find_element(By.CLASS_NAME, 'e19owgy710')
        startbtn.click()
        
        self.get_num()
