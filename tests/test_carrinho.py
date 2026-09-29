from pages.pagina_carrinho import PaginaCarrinho
from playwright.sync_api import expect

def test_carrinho_adicionar_carrinho(page):
    paginacarrinho = PaginaCarrinho(page)
    paginacarrinho.acessar_home()
    paginacarrinho.card_produto.first.click()
    page.wait_for_timeout(1000)
    paginacarrinho.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()
    paginacarrinho.acessar_carrinho()
    expect(paginacarrinho.campo_cart_quantity).to_have_value("1")
    paginacarrinho.acessar_home()
    paginacarrinho.card_produto.first.click()
    page.wait_for_timeout(1000)
    paginacarrinho.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()
    paginacarrinho.acessar_carrinho()
    expect(paginacarrinho.campo_cart_quantity).to_have_value("2")

def test_carrinho_alterar_quantidade(page):
    paginacarrinho = PaginaCarrinho(page)
    paginacarrinho.acessar_home()
    paginacarrinho.card_produto.first.click()
    page.wait_for_timeout(1000)
    paginacarrinho.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()
    paginacarrinho.acessar_carrinho()
    expect(paginacarrinho.campo_cart_quantity).to_have_value("1")
    paginacarrinho.campo_cart_quantity.fill("5")
    paginacarrinho.campo_cart_quantity.press("Tab")
    expect(page.get_by_text("Product quantity updated.", exact=True)).to_be_visible()
    preco_unitario = paginacarrinho.texto_preco_produto.text_content()
    preco_unitario = float(preco_unitario.replace("$", ""))
    preco_total = float(paginacarrinho.texto_total_produto.text_content().replace("$", ""))
    assert preco_total == preco_unitario*5, "O preço total é diferente do preço do produto multiplicado pela quantidade"

def test_carrinho_remover_produto(page):
    paginacarrinho = PaginaCarrinho(page)
    paginacarrinho.acessar_home()
    paginacarrinho.card_produto.first.click()
    page.wait_for_timeout(1000)
    paginacarrinho.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()
    paginacarrinho.acessar_home()
    paginacarrinho.card_produto.nth(1).click()
    page.wait_for_timeout(1000)
    paginacarrinho.adicionar_carrinho.click()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("Product added to shopping cart.", exact=True)).to_be_visible()
    paginacarrinho.acessar_carrinho()
    expect(paginacarrinho.texto_preco_produto).to_have_count(2)
    page.locator(".btn-danger").nth(1).click()
    expect(page.get_by_text("Product deleted.", exact=True)).to_be_visible()
    expect(paginacarrinho.texto_preco_produto).to_have_count(1)

def test_acessar_carrinho_vazio(page):
    paginacarrinho = PaginaCarrinho(page)
    paginacarrinho.acessar_carrinho()
    expect(page.get_by_text("Quantity" )).not_to_be_visible()
    expect(page.get_by_text("Price" )).not_to_be_visible()
    expect(page.get_by_text("Total" )).not_to_be_visible()
    expect(page.get_by_text("Proceed to checkout" )).not_to_be_visible()





