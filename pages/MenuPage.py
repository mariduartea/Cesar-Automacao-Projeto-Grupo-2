from pages.Base import Base
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

class MenuPage(Base):

    menu_icon = (By.CLASS_NAME, 'oxd-navbar-nav')
    myinfo = (By.CSS_SELECTOR, '[href="/web/index.php/pim/viewMyDetails"]')
    buzz = (By.CSS_SELECTOR, '[href="/web/index.php/buzz/viewBuzz"]')

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def has_menu_icon(self):
        try:
            menu_element = self.wait_element(self.menu_icon)
            return menu_element.is_displayed()
        except NoSuchElementException:
            return False

    def click_info(self):
        self.wait_element(self.myinfo).click()

    def click_buzz(self):
        self.wait_element(self.buzz).click()