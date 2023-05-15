import typing

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from sys import platform

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages import *

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

loginObj = login.Login(driver)


def menu():
    os.system("cls" if platform == "win32" else "clear")
    choice = int(input("1. Verbal Memory\n2. Typing (NF)\n3. Chimp Test\n> "))

    match choice:
        case 1:
            vm = verbal_memory.VerbalMemory(driver)
            vm.start()
        case 2:
            typing_test_object = typing_test.Typing(driver)
            typing_test_object.start()
        case 3:
            chimp = chimp_test.Chimp(driver)
            chimp.start()
        case _:
            pass

    menu()


if __name__ == "__main__":
    loginObj.start()

    menu()
