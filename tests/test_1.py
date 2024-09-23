from pages.BuzzPage import BuzzPage
from pages.MenuPage import MenuPage

class Test1:

    def test_new_post_buzz(self, login_orange):

        description = "Teste uma nova postagem na tela Buzz. Time 2"
        login_p = login_orange
        menu = MenuPage(driver=login_p.driver)
        assert menu.has_menu_icon(), "Elemento não encontrado"
        menu.click_buzz()
        buzz = BuzzPage(driver=menu.driver)
        assert buzz.is_url_buzz(), "URL inválida"
        buzz.input_text(description)
        buzz.click_post_button()
        assert login_p.alerts(), "Alert não encontrado"
        assert buzz.has_description_post() == description, "Elemento não encontrado"