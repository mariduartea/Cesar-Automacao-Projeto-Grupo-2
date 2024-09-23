from pages.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BuzzPage(Base):

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'
    input_description_post = (By.CSS_SELECTOR, '.oxd-buzz-post-input')
    btn_post = (By.CSS_SELECTOR, '[class="oxd-button oxd-button--medium oxd-button--main"]')
    has_post = (By.CSS_SELECTOR, '[class="oxd-sheet oxd-sheet--rounded oxd-sheet--white orangehrm-buzz"]')
    has_text_post = (By.CSS_SELECTOR, '[class="oxd-text oxd-text--p orangehrm-buzz-post-body-text"]')
    btn_three_points =(By.CSS_SELECTOR, '[class="oxd-icon bi-three-dots"]')
    modal = (By.CSS_SELECTOR, '.orangehrm-dialog-modal')
    edit_option = (By.CSS_SELECTOR, '[class="oxd-icon bi-pencil"]')
    delete_option = (By.CSS_SELECTOR, '[class="oxd-icon bi-trash"]')
    delete_confirm = (By.CSS_SELECTOR, '[class="oxd-icon bi-trash oxd-button-icon"]')
    comment_icon = (By.CSS_SELECTOR, '[class="oxd-icon bi-chat-text-fill"]')
    comment_text = (By.CSS_SELECTOR, '[placeholder="Write your comment..."]')
    like_icon = (By.CSS_SELECTOR, '[class="orangehrm-buzz-post-actions"] [class="orangehrm-heart-icon"]')
    like_interactions_active = (By.CSS_SELECTOR, '[class="orangehrm-buzz-post-actions"] [class="orangehrm-like-animation"]')
    share_icon = (By.CSS_SELECTOR, '[class="oxd-icon bi-share-fill"]')
    interaction_active = (By.CSS_SELECTOR, '[class="oxd-text oxd-text--p orangehrm-buzz-stats-active"]')

    def __init__(self, driver):
        super(BuzzPage, self).__init__(driver=driver)

    def is_url_buzz(self):
        return self.is_url(self.url)

    def input_text(self, description):
        self.wait_element(self.input_description_post).send_keys(description)

    def click_post_button(self):
        self.driver.find_element(*self.btn_post).click()

    def edit_post(self, description):
        self.wait_element(self.btn_three_points).click()
        self.wait_element(self.edit_option).click()
        modal = self.wait_element(self.modal)
        input_post = modal.find_element(*self.input_description_post)
        input_post.send_keys(Keys.BACKSPACE * len(input_post.get_attribute("value")))
        input_post.send_keys(description)
        modal.find_element(*self.btn_post).click()

    def delete_post(self):
        self.wait_element(self.btn_three_points).click()
        self.wait_element(self.delete_option).click()
        self.wait_element(self.delete_confirm).click()

    def comment_post(self, comment):
        self.wait_element(self.comment_icon).click()
        self.wait_element(self.comment_text).send_keys(comment, Keys.ENTER)

    def like_post(self):
        self.wait_element(self.like_icon).click()

    def share_post(self):
        self.wait_element(self.share_icon).click()
        modal_share = self.wait_element(self.modal)
        modal_share.find_element(*self.btn_post).click()

    def get_post(self, position = 0):
        post = self.driver.find_elements(*self.has_post)
        return post[position]

    def has_description_post(self):
        return self.wait_element(self.has_text_post).text

    def has_like_interactions(self):
        return self.get_post().find_element(*self.like_interactions_active).is_displayed()

    def has_interactions(self):
        return self.get_post().find_element(*self.interaction_active).text

    def has_share(self):
        element = self.get_post(1).find_elements(*self.interaction_active)
        element_position = element[1]
        return element_position.text

    def get_post_by_text(self, text):
        post = self.get_post()
        return post.find_elements(By.XPATH, f"//p[text()='{text}']")