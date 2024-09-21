import pytest

from pages.LoginPage import LoginPage

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
def login_saucedemo(open_browser):
    login_p = open_browser
    login_p.efetuar_login()

