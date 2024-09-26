import random
import time

from pages.InfoPage import InfoPage
from pages.MenuPage import MenuPage
from pages.QualificationPage import QualificationPage


class Test9:

    def test_delete_record_on_the_qualification_screen(self, login_orange):
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

        # preenchendo os campos Company, Job, Title, From e To e garantindo que foram preenchidos
        labels = ['Company', 'Job Title', 'From', 'To']
        input_values = ['Company Teste', 'QA', '2023-01-09', '2024-01-09']

        for label, value in zip(labels, input_values):
            qualification_p.enter_value(label, value)

            filled_value = qualification_p.get_value_by_label(label)
            assert filled_value == value, f"O campo '{label}' deveria ter '{value}', mas tem '{filled_value}'"

        # preenchendo o campos Comment e garantindo que foi preenchido
        label = 'Comment'
        textarea = 'Deletando um item'
        qualification_p.enter_comment(label, textarea)
        time.sleep(1)

        filled_comment = qualification_p.get_comment('Comment')
        assert filled_comment == textarea, f"O campo '{label}' deveria ter '{textarea}' mas tem '{filled_comment}'"

        # Salvando os valores preenchidos
        qualification_p.save_values()
        time.sleep(5)

        num_trash_icons_before = len(qualification_p.get_trash_icons())
        print(num_trash_icons_before)
        qualification_p.delete_item(0)
        time.sleep(5)
        num_trash_icons_after = len(qualification_p.get_trash_icons())
        print(num_trash_icons_after)

        assert num_trash_icons_before - 1, 'Nenhum item foi excluído'


