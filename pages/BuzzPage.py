from pages.Base import Base
from selenium.webdriver.common.by import By

class BuzzPage(Base):

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'
    element_post = (By.CSS_SELECTOR, '[placeholder="What\'s on your mind?"]')
    password_field = (By.CSS_SELECTOR, '[name="password"]')
    post_btn = (By.CSS_SELECTOR, '.oxd-buzz-post-slot > button')

    def __init__(self, driver):
        super(BuzzPage, self).__init__(driver=driver)

    def is_url_buzz(self):
        return self.is_url(self.url)

    def new_post(self, description):
        self.wait_element(self.element_post).send_keys(description)

    def click_post_button(self):
        self.driver.find_element(*self.post_btn).click()

