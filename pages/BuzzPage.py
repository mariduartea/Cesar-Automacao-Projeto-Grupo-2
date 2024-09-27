import time
from pages.Base import Base
from interaction_type import InteractionType
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
    interaction_active = (By.CSS_SELECTOR, '.orangehrm-buzz-stats .oxd-text--p')

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
        counter = 0
        while counter < 10:
            posts = self.driver.find_elements(*self.has_post)
            if len(posts) > 0:
                return posts[position]
            time.sleep(1)
            counter += 1
        return None

    def has_description_post(self, text_post):
        counter = 0
        while counter < 10:
            if self.wait_element(self.has_text_post).text == text_post:
                return True
            time.sleep(1)
            counter += 1
        return False

    def has_like_interactions(self):
        post = self.get_post()
        counter = 0
        while counter < 10:
            like_active = post.find_elements(*self.like_interactions_active)
            if len(like_active):
                return like_active[0].is_displayed()
            time.sleep(1)
            counter += 1
        return False

    def has_interactions(self, type: InteractionType, text, post_number: int = 0):
        time.sleep(1)
        post = self.get_post(post_number)
        elements = post.find_elements(*self.interaction_active)
        interaction = elements[type.value]
        counter = 0
        while counter < 10:
            if interaction.text == text:
                return True
            time.sleep(1)
            counter += 1
        return False

    def get_posts_by_text(self, text):
        counter = 0
        while counter < 5:
            time.sleep(1)
            posts = self.driver.find_elements(By.XPATH, f"//p[text()='{text}']")
            if len(posts) > 0:
                return posts
            counter += 1
        return []