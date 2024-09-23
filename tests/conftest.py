import pytest

from pages.BuzzPage import BuzzPage
from pages.LoginPage import LoginPage
from pages.MenuPage import MenuPage

def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help='Select browser to run testes')

@pytest.fixture
def open_browser(request):
    selected_browser = request.config.getoption('browser').lower()
    login_p = LoginPage(browser=selected_browser)
    login_p.open_login()
    yield login_p
    login_p.close()

@pytest.fixture
def login_orange(open_browser):
    login_p = open_browser
    login_p.efetuar_login()
    yield login_p

@pytest.fixture
def new_post_buzz(login_orange):
    description = "Nova postagem para realizar testes. Time 2."
    login_p = login_orange
    menu_p = MenuPage(driver=login_p.driver)
    assert menu_p.has_menu_icon(), "Elemento não encontrado"
    menu_p.click_buzz()
    buzz_p = BuzzPage(driver=menu_p.driver)
    assert buzz_p.is_url_buzz(), "URL inválida"
    buzz_p.input_text(description)
    buzz_p.click_post_button()
    assert login_p.alerts(), "Alert não encontrado"
    assert buzz_p.has_description_post() == description, "Elemento não encontrado"
    yield login_p, menu_p, buzz_p