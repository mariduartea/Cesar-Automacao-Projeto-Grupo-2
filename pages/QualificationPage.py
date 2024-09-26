from selenium.webdriver.common.by import By

from pages.Base import Base

class QualificationPage(Base):

    qualification_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewQualifications/empNumber/7'
    qualification_menu = (By.LINK_TEXT, "Qualifications")
    add_new_wk_btn = (By.XPATH, "//h6[text()='Work Experience']/following::button[contains(@class, 'oxd-button')]")
    save_btn = (By.CSS_SELECTOR, '.oxd-button[type="submit"]')
    input_group = (By.CLASS_NAME, 'oxd-input-group')
    label_name = (By.CLASS_NAME, 'oxd-label')
    input_field = (By.CLASS_NAME, "oxd-input")
    textarea_input = (By.CLASS_NAME, "oxd-textarea")
    table_header_cell = (By.CLASS_NAME, 'oxd-table-header-cell')
    table_value_cell = (By.CLASS_NAME, 'oxd-table-cell')
    span_text = (By.CLASS_NAME, 'oxd-text--span')
    trash_btn = (By.CLASS_NAME, 'bi-trash')
    trash_confirm_btn = (By.CSS_SELECTOR, '.oxd-button.oxd-button--medium.oxd-button--label-danger')

    def __init__(self, driver):
        super(QualificationPage, self).__init__(driver=driver)

    def click_qualification_menu(self):
        self.driver.find_element(*self.qualification_menu).click()

    def is_qualification_url(self):
        return self.is_url(self.qualification_url)

    def add_new_work_experience(self):
        self.driver.find_element(*self.add_new_wk_btn).click()

    # função para preencher os campos Company, Job, Title, From e To
    def enter_value(self, label, input_value):
        grid_items = self.driver.find_elements(*self.input_group)
        for item in grid_items:
            if item.find_element(*self.label_name).text == label:
                item.find_element(*self.input_field).send_keys(input_value)
                break

    # função para validar os valores dos campos preenchidos (Company, Job, Title, From e To)
    def get_value_by_label(self, label):
        grid_items = self.driver.find_elements(*self.input_group)
        for item in grid_items:
            if item.find_element(*self.label_name).text == label:
                input_element = item.find_element(*self.input_field)
                return input_element.get_attribute('value')

    # função para preencher o campo Comment
    def enter_comment(self, label, textarea):
        grid_items = self.driver.find_elements(*self.input_group)
        for item in grid_items:
            if item.find_element(*self.label_name).text == label:
                item.find_element(*self.textarea_input).send_keys(textarea)
                break

    # função para validar o valor do campo Comment
    def get_comment(self, label):
        grid_items = self.driver.find_elements(*self.input_group)
        for item in grid_items:
            if item.find_element(*self.label_name).text.strip() == label:
                input_element = item.find_element(*self.textarea_input)
                return input_element.get_attribute('value')

    # função para salvar o formulário
    def save_values(self):
        self.driver.find_element(*self.save_btn).click()

    # função para verificar que os valores enviados estão corretamente listador em Record Found
    def table_content(self, label, expected_values):
        record_header = self.driver.find_elements(*self.table_header_cell)
        for item in record_header:
            if item.text == label:
                value_elements = self.driver.find_elements(*self.table_value_cell)
                for value_element in value_elements:
                    if value_element.text == expected_values:
                        return value_element.text

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
                return error_message

    # função para excluir registro
    def delete_item(self, index):
        delete_button = self.driver.find_elements(*self.trash_btn)
        element = delete_button[index]
        element.click()
        self.driver.find_element(*self.trash_confirm_btn).click()

    def get_trash_icons(self):
        return self.driver.find_elements(*self.trash_btn)
