import os
import time
from pathlib import Path

from playwright.sync_api import sync_playwright
import pytest

from pages.pagina_cadastro import PaginaCadastro
from pages.pagina_login import PaginaLogin

SENHA_PADRAO = "1HgJx2d45#"


def gerar_email_unico(prefixo="higtest"):
    return f"{prefixo}{int(time.time() * 1000)}@test.com"


HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
PASTA_SCREENSHOTS = Path("relatorio/screenshots")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Guarda o resultado de cada fase no item, para o fixture `page` saber se o teste falhou.
    resultado = yield
    relatorio = resultado.get_result()
    setattr(item, f"resultado_{relatorio.when}", relatorio)


@pytest.fixture(scope="session")
def navegador(request):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=HEADLESS,
            args=["--disable-blink-features=AutomationControlled"],
        )
        yield browser
        browser.close()

@pytest.fixture
def page(navegador, request):
    opcoes = {"base_url": "https://practicesoftwaretesting.com/"}
    if HEADLESS:
        # O user agent padrão do modo headless contém "HeadlessChrome", o que faz o
        # Cloudflare do site bloquear/desafiar o navegador (principalmente a partir do CI).
        opcoes["user_agent"] = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            f"(KHTML, like Gecko) Chrome/{navegador.version} Safari/537.36"
        )
        opcoes["viewport"] = {"width": 1920, "height": 1080}
    contexto = navegador.new_context(**opcoes)
    pagina = contexto.new_page()
    yield pagina
    resultado = getattr(request.node, "resultado_call", None)
    if resultado is not None and resultado.failed:
        PASTA_SCREENSHOTS.mkdir(parents=True, exist_ok=True)
        pagina.screenshot(path=PASTA_SCREENSHOTS / f"{request.node.name}.png", full_page=True)
        print(f"URL: {pagina.url} | Título: {pagina.title()}")
    contexto.close()


@pytest.fixture
def novo_usuario(page):
    """Cadastra um usuário com email único e retorna suas credenciais, sem fazer login."""
    email = gerar_email_unico()
    paginacadastro = PaginaCadastro(page)
    paginacadastro.acessar_cadastro()
    paginacadastro.preencher_cadastro(primeiro_nome='Hig', ultimo_nome='Teste', data_nascimento='2000-06-25',
                                      pais='Brazil', cep='1234567', numero_casa='124', rua='Avenida Atlântica',
                                      cidade='Rio de Janeiro',
                                      estado='RJ', telefone='21567846845', email=email, senha=SENHA_PADRAO)
    paginacadastro.botao_cadastrar.click()
    page.wait_for_timeout(1000)
    return {"email": email, "senha": SENHA_PADRAO}


@pytest.fixture
def usuario_logado(page, novo_usuario):
    """Cadastra um usuário novo e já efetua login com as credenciais dele."""
    paginalogin = PaginaLogin(page)
    paginalogin.acessar_login()
    paginalogin.preencher_login(email=novo_usuario["email"], senha=novo_usuario["senha"])
    paginalogin.botao_login.click()
    page.wait_for_timeout(1000)
    return novo_usuario
