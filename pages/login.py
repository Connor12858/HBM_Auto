from selenium.webdriver.common.by import By


class Login:
    def __init__(self, _driver):
        self.driver = _driver

    def start(self):
        #user = input("Username: ")
        #pwd = input("Password: ")

        user = "connor12858"
        pwd = 'CJDrake1!'

        self.driver.get('https://humanbenchmark.com/login')

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(user)

        pwd_input = self.driver.find_element(By.NAME, "password")
        pwd_input.send_keys(pwd)

        login_button = self.driver.find_element(By.CLASS_NAME, 'e19owgy712')
        login_button.click()

