# Import the needed packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from pages import *

driver = webdriver.Chrome("chromedriver.exe")

loginObj = login.Login(driver)

if __name__ == "__main__":
    loginObj.start()

    print("Test 1 - Verbal Memory")
    vm = verbal_memory.VerbalMemory(driver)
    vm.start()
    print("Running...")

    print("Test 2 - Typing Test")
    typing_test_object = typing_test.Typing(driver)
    typing_test_object.start()
    print("Running...")

    print("Test 3 - Chimp Test")
    chimp = chimp_test.Chimp(driver)
    chimp.start()
    print("Running...")

    print("Test 4 - Number Memory")
    number = number_memory.NumberMemory(driver)
    number.start()
    print("Running...")

    print("Test 5 - Reaction Time")
    reaction = reaction.Reaction(driver)
    reaction.start()
    print("Running...")

    print("Test 6 - Aim Trainer")
    aim = aim.Aim(driver)
    aim.start()
    print("Running...")

