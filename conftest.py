from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="session")
def navegador(request):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(navegador):
    contexto = navegador.new_context(base_url="https://practicesoftwaretesting.com/")
    pagina = contexto.new_page()
    yield pagina
    contexto.close()