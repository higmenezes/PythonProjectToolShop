import time
from pages.pagina_cadastro import PaginaCadastro
from pages.pagina_login import PaginaLogin
from pages.pagina_checkout import PaginaCheckout
from playwright.sync_api import expect

SENHA_PADRAO = "1HgJx2d45#"


def gerar_email_unico():
    return f"higcheckout{int(time.time() * 1000)}@test.com"


def cadastrar_e_logar(page, email, senha=SENHA_PADRAO):
    paginacadastro = PaginaCadastro(page)
    paginacadastro.acessar_cadastro()
    paginacadastro.preencher_cadastro(primeiro_nome='Hig', ultimo_nome='Checkout', data_nascimento='2000-06-25',
                                      pais='Brazil', cep='1234567', numero_casa='124', rua='Avenida Atlântica',
                                      cidade='Rio de Janeiro',
                                      estado='RJ', telefone='21567846845', email=email, senha=senha)
    paginacadastro.botao_cadastrar.click()
    page.wait_for_timeout(1000)

    paginalogin = PaginaLogin(page)
    paginalogin.acessar_login()
    paginalogin.preencher_login(email=email, senha=senha)
    paginalogin.botao_login.click()
    page.wait_for_timeout(1000)


def test_checkout_completo_com_sucesso(page):
    cadastrar_e_logar(page, gerar_email_unico())

    paginacheckout = PaginaCheckout(page)
    paginacheckout.acessar_home()
    paginacheckout.card_produto.first.click()
    page.wait_for_timeout(1000)
    paginacheckout.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()

    paginacheckout.acessar_carrinho()
    paginacheckout.prosseguir_para_checkout()
    expect(page.get_by_text("you are already logged in", exact=False)).to_be_visible()
    paginacheckout.confirmar_login_no_checkout()

    paginacheckout.preencher_endereco_entrega(pais="United States of America (the)", cep="10001",
                                              numero_casa="124", rua="5th Avenue", cidade="New York", estado="NY")
    expect(paginacheckout.botao_prosseguir_endereco).to_be_enabled()
    paginacheckout.prosseguir_para_pagamento()

    paginacheckout.selecionar_forma_pagamento("Cash on Delivery")
    paginacheckout.finalizar_pedido()
    expect(paginacheckout.texto_pagamento_sucesso).to_be_visible()
    paginacheckout.finalizar_pedido()
    expect(page.get_by_text("Thanks for your order!", exact=False)).to_be_visible()


def test_checkout_carrinho_vazio(page):
    cadastrar_e_logar(page, gerar_email_unico())

    paginacheckout = PaginaCheckout(page)
    paginacheckout.acessar_carrinho()
    expect(page.get_by_text("Quantity")).not_to_be_visible()
    expect(page.get_by_text("Price")).not_to_be_visible()
    expect(page.get_by_text("Total")).not_to_be_visible()
    expect(page.get_by_text("Proceed to checkout")).not_to_be_visible()


def test_checkout_endereco_incompleto(page):
    cadastrar_e_logar(page, gerar_email_unico())

    paginacheckout = PaginaCheckout(page)
    paginacheckout.acessar_home()
    paginacheckout.card_produto.first.click()
    page.wait_for_timeout(1000)
    paginacheckout.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()

    paginacheckout.acessar_carrinho()
    paginacheckout.prosseguir_para_checkout()
    paginacheckout.confirmar_login_no_checkout()

    paginacheckout.preencher_endereco_entrega(pais="United States of America (the)", cep="10001",
                                              numero_casa="", rua="5th Avenue", cidade="New York", estado="NY")
    expect(paginacheckout.botao_prosseguir_endereco).to_be_disabled()
    expect(page.get_by_role("heading", name="Billing Address")).to_be_visible()


def test_checkout_sem_estar_logado(page):
    paginacheckout = PaginaCheckout(page)
    paginacheckout.acessar_home()
    paginacheckout.card_produto.first.click()
    page.wait_for_timeout(1000)
    paginacheckout.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()

    paginacheckout.acessar_carrinho()
    paginacheckout.prosseguir_para_checkout()
    expect(paginacheckout.input_email_checkout).to_be_visible()
    expect(paginacheckout.link_cadastro_checkout).to_be_visible()
    expect(paginacheckout.select_pais_endereco).not_to_be_visible()


def test_checkout_resumo_reflete_itens_do_carrinho(page):
    cadastrar_e_logar(page, gerar_email_unico())

    paginacheckout = PaginaCheckout(page)
    paginacheckout.acessar_home()
    paginacheckout.card_produto.first.click()
    page.wait_for_timeout(1000)
    paginacheckout.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()

    paginacheckout.acessar_home()
    paginacheckout.card_produto.nth(1).click()
    page.wait_for_timeout(1000)
    paginacheckout.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()

    paginacheckout.acessar_carrinho()
    expect(paginacheckout.texto_preco_produto).to_have_count(2)
    precos_unitarios = [float(p.replace("$", "")) for p in paginacheckout.texto_preco_produto.all_text_contents()]
    precos_totais = [float(p.replace("$", "")) for p in paginacheckout.texto_total_produto.all_text_contents()]
    total_esperado = sum(precos_unitarios)
    total_exibido = float(paginacheckout.texto_total_carrinho.text_content().replace("$", ""))
    assert precos_unitarios == precos_totais, "Preço total de cada linha deveria ser igual ao preço unitário (quantidade 1)"
    assert total_exibido == total_esperado, "Total do carrinho não corresponde à soma dos itens adicionados"
