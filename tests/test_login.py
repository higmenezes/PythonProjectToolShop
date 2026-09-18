from pages.pagina_login import PaginaLogin
from playwright.sync_api import expect

def test_pagina_login(page):
    paginalogin = PaginaLogin(page)
    paginalogin.acessar_login()
    paginalogin.preencher_login(email="higtest22@test.com", senha="1HgJx2d45#")
    paginalogin.botao_login.click()
    expect(page.get_by_text("My account", exact=True)).to_be_visible()

def test_pagina_login_senha_incorreta(page):
    paginalogin = PaginaLogin(page)
    paginalogin.acessar_login()
    paginalogin.preencher_login(email="higtest22@test.com", senha="1HgJx2d45#f")
    paginalogin.botao_login.click()
    expect(page.get_by_text("Invalid email or password")).to_be_visible()

def test_pagina_login_email_inexistente(page):
    paginalogin = PaginaLogin(page)
    paginalogin.acessar_login()
    paginalogin.preencher_login(email="higtdddest22@test.com", senha="1HgJx2d45#f")
    paginalogin.botao_login.click()
    expect(page.get_by_text("Invalid email or password")).to_be_visible()

def test_pagina_login_campos_vazios(page):
    paginalogin = PaginaLogin(page)
    paginalogin.acessar_login()
    paginalogin.preencher_login(email="", senha="")
    paginalogin.botao_login.click()
    expect(page.get_by_text("Email is required")).to_be_visible()
    expect(page.get_by_text("Password is required")).to_be_visible()




