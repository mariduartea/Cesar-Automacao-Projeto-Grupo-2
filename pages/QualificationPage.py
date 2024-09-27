from pages.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class QualificationPage(Base):

    qualification_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewQualifications/empNumber/7'
    qualification_menu = (By.LINK_TEXT, "Qualifications")
    add_new_wk_btn = (By.XPATH, "//h6[text()='Work Experience']/following::button[contains(@class, 'oxd-button')]")
    save_btn = (By.CSS_SELECTOR, '.oxd-button[type="submit"]')
    input_group = (By.CLASS_NAME, 'oxd-input-group')
    label_name = (By.CLASS_NAME, 'oxd-label')
    input_field = (By.CLASS_NAME, "oxd-input")
    table_row = (By.CSS_SELECTOR, '.oxd-table-row')
    table_value_cell = (By.CLASS_NAME, 'oxd-table-cell')
    span_text = (By.CLASS_NAME, 'oxd-text--span')
    trash_btn = (By.CLASS_NAME, 'bi-trash')
    trash_confirm_btn = (By.CSS_SELECTOR, '.oxd-button.oxd-button--medium.oxd-button--label-danger')
    spinner = (By.CSS_SELECTOR, '[class="oxd-loading-spinner-container"] [class="oxd-loading-spinner"]')

    def __init__(self, driver):
        super(QualificationPage, self).__init__(driver=driver)

    def is_qualification_url(self):
        return self.is_url(self.qualification_url)

    def click_qualification_menu(self):
        self.wait_element(self.qualification_menu).click()

    def add_new_work_experience(self):
        self.wait_element(self.add_new_wk_btn).click()

    # função para preencher os campos Company, Job, Title, From e To
    def enter_value(self, label, input_value):
        grid_items = self.driver.find_elements(*self.input_group)
        for item in grid_items:
            if item.find_element(*self.label_name).text == label:
                item.find_element(*self.input_field).send_keys(input_value)
                break

    # função para salvar o formulário
    def save_values(self):
        self.wait_element(self.save_btn).click()

    # função para verificar que os valores enviados estão corretamente listador em Record Found                    
    def was_saved(self, expected_values):
        table_rows = self.driver.find_elements(*self.table_row)
        cells = table_rows[1].find_elements(*self.table_value_cell)[1:5]

        if len(cells) == 0:
            return False

        for value, cell in zip(expected_values, cells):
            if cell.text != value:
                return False
        return True

    # função para verificar que o erro Required é exibida para os campos obrigatórios
    def error_message_for_required_fields(self, field_label):
        field_required = None
        grid_items = self.driver.find_elements(*self.input_group)
        for item in grid_items:
            if item.find_element(*self.label_name).text == field_label:
                field_required = item
                break

        if field_required:
                error_message = field_required.find_element(*self.span_text).text
                return error_message == 'Required'

    # função para excluir registro
    def delete_item(self, index):
        delete_button = self.driver.find_elements(*self.trash_btn)
        element = delete_button[index]
        element.click()
        self.driver.find_element(*self.trash_confirm_btn).click()

    def wait_spinner(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element_located((self.spinner)))