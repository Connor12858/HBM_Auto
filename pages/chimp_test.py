from selenium.webdriver.common.by import By


class Chimp:
    def __init__(self, driver):
        self.driver = driver
        self.grid = []
        self.count = 4

    def get_item(self, num):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y].text == str(num):
                    return self.grid[x][y]

    def keep_going(self):
        btn = self.driver.find_element(By.CLASS_NAME, "e19owgy710")
        btn.click()

        self.count += 1
        self.grid = []
        self.get_grid()

    def click_order(self):
        for i in range(self.count):
            num = i + 1
            item = self.get_item(num)
            item.click()

        self.keep_going()

    def get_grid(self):
        rows = self.driver.find_elements(By.CLASS_NAME, 'css-k008qs')

        for i in range(len(rows)):
            div_elems = rows[i].find_elements(By.TAG_NAME, "div")
            self.grid.append([])
            for z in range(len(div_elems)):
                if "css" in div_elems[z].get_attribute("class"):
                    self.grid[i].append(div_elems[z])

        self.click_order()

    def start(self):
        self.driver.get("https://humanbenchmark.com/tests/chimp")

        start_btn = self.driver.find_element(By.CLASS_NAME, 'e19owgy710')
        start_btn.click()

        self.get_grid()
