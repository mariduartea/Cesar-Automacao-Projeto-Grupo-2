import time

from pages.InfoPage import InfoPage
from pages.MenuPage import MenuPage
from pages.QualificationPage import QualificationPage


class Test8:

    def test_validation_of_mandatory_fields(self, login_orange):
        login_p = login_orange
        menu = MenuPage(driver=login_p.driver)
        assert menu.has_menu_icon(), "Elemento não encontrado"
        menu.click_info()

        myinfo = InfoPage(driver=login_p.driver)
        assert myinfo.is_url_myinfo(), "URL inválida"

        time.sleep(2)
        qualification_p = QualificationPage(driver=login_p.driver)
        qualification_p.click_qualification_menu()
        assert qualification_p.is_qualification_url(), 'URL inválida'
        time.sleep(2)

        qualification_p.add_new_work_experience()
        time.sleep(1)

        # Salvando sem preencher os campos
        qualification_p.save_values()
        time.sleep(1)

        # Verificar se as mensagens de Required são exibidas para os campos Company e Job Title
        company_error = qualification_p.error_message_for_required_fields('Company')
        assert company_error == 'Required', 'Mensagem de obrigatoriedade de preenchimento do campo Company não foi exibida'

        job_title_error = qualification_p.error_message_for_required_fields('Job Title')
        assert job_title_error == 'Required', 'Mensagem de obrigatoriedade de preenchimento do campo Job Title não foi exibida'



