import time

from selenium.webdriver.common.by import By

from pages.Base import Base

class LoginPage(Base):

    url_login = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    username_field = (By.CSS_SELECTOR, '[name="username"]')
    password_field = (By.CSS_SELECTOR, '[name="password"]')
    login_btn = (By.TAG_NAME, 'button')

    def __init__(self, browser):
        super(LoginPage, self).__init__(driver=None, browser=browser)

    def open_login(self):
        self.driver.get(self.url_login)

    def click_login_button(self):
        self.driver.find_element(*self.login_btn)

    def efetuar_login(self, username='Admin', password='admin123'):
        time.sleep(5)
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.click_login_button()