from pages.InfoPage import InfoPage
from pages.MenuPage import MenuPage

class Test8:

    def test_validation_of_mandatory_fields(self, login_orange):
        login_p = login_orange
        menu = MenuPage(driver=login_p.driver)
        assert menu.has_menu_icon(), "Elemento não encontrado"
        menu.click_info()

        myinfo = InfoPage(driver=login_p.driver)
        assert myinfo.is_url_myinfo(), "URL inválida"
