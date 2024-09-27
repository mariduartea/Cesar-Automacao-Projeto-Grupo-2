from pages.BuzzPage import BuzzPage
from pages.MenuPage import MenuPage

class Test1:

    def test_new_post_buzz(self, login_orange):

        login_p = login_orange

        description = "Uma nova postagem na tela Buzz. Time 2"

        menu_p = MenuPage(driver=login_p.driver)
        assert menu_p.has_menu_icon(), "Elemento não encontrado"
        menu_p.click_buzz()
        buzz_p = BuzzPage(driver=menu_p.driver)
        assert buzz_p.is_url_buzz(), "URL inválida"
        buzz_p.input_text(description)
        buzz_p.click_post_button()
        assert login_p.alerts(), "Alert não encontrado"
        assert buzz_p.has_description_post(description), "Elemento não encontrado"

        # Como este teste é sobre o cadastro de um post, eu não estou usando o new_post_buzz_with_delete do conftest
        buzz_p.delete_post()
        assert login_p.alerts(), "Alert não encontrado"