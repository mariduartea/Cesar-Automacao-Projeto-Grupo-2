from selenium import webdriver


class Base:

    def __init__(self, driver, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise Exception('Browser não suportado')

    def is_url(self, url):
        return self.driver.current_url == url

    def close(self):
        self.driver.quit()