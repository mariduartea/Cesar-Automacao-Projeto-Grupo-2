from pages.InfoPage import InfoPage
from pages.MenuPage import MenuPage

class Test9:

    def test_delete_record_on_the_qualification_screen(self, login_orange):
        login_p = login_orange
        menu = MenuPage(driver=login_p.driver)
        assert menu.has_menu_icon(), "Elemento não encontrado"
        menu.click_info()

        myinfo = InfoPage(driver=login_p.driver)
        assert myinfo.is_url_myinfo(), "URL inválida"
