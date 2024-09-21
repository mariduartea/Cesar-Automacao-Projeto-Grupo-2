from pages.BuzzPage import BuzzPage
from pages.MenuPage import MenuPage

class Test2:

    def test_edit_post_buzz(self, login_orange):
        login_p = login_orange
        menu = MenuPage(driver=login_p.driver)
        assert menu.has_menu_icon(), "Elemento não encontrado"
        menu.click_buzz()

        buzz = BuzzPage(driver=login_p.driver)
        assert buzz.is_url_buzz(), "URL inválida"
