from selenium.webdriver.common.by import By


class Chimp:
    def __init__(self, driver):
        self.driver = driver
        self.count = 4

    def keep_going(self):
        btn = self.driver.find_element(By.CLASS_NAME, "e19owgy710")
        btn.click()

        self.count += 1
        if self.count < 40:
            self.get_grid()

    def get_grid(self):
        canContinue = True
        for i in range(self.count):
            rows = self.driver.find_elements(By.CLASS_NAME, 'css-k008qs')
            for r in rows:
                if canContinue:
                    cols = []
                    divs = r.find_elements(By.TAG_NAME,'div')
                    for div in divs:
                        if "css" in div.get_attribute("class"):
                            cols.append(div)
                    for c in cols:
                        attri = c.get_attribute("data-cellnumber")
                        if attri != None:
                            if int(attri) == i + 1:
                                c.click()
                                if i + 1 == self.count:
                                    canContinue = False
                                break
                else:
                    break
        self.keep_going()

    def start(self):
        self.driver.get("https://humanbenchmark.com/tests/chimp")

        start_btn = self.driver.find_element(By.CLASS_NAME, 'e19owgy710')
        start_btn.click()

        self.get_grid()
