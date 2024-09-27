from pages.Base import Base
from selenium.webdriver.common.by import By

class InfoPage(Base):

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7'

    def __init__(self, driver):
        super(InfoPage, self).__init__(driver=driver)

    def is_url_myinfo(self):
        return self.is_url(self.url)