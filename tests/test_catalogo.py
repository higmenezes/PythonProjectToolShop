from pages.pagina_catalogo import PaginaCatalogo
from playwright.sync_api import expect

def test_catalogo_busca_produto_existente(page):
    paginacatalogo = PaginaCatalogo(page)
    paginacatalogo.acessar_home()
    paginacatalogo.input_busca.fill("hammer")
    paginacatalogo.botao_busca.click()
    expect(page.get_by_text("Searched for: hammer")).to_be_visible()
    quantidade = paginacatalogo.card_produto.count()
    assert quantidade > 0, f'Quantidade não é maior que zero'
    print(f'Quantidade: {quantidade}')
    page.pause()

def test_catalogo_busca_termo_inexistente(page):
    paginacatalogo = PaginaCatalogo(page)
    paginacatalogo.acessar_home()
    paginacatalogo.buscar_produto("hXwrglzd")
    expect(page.get_by_text("Searched for: hXwrglzd")).to_be_visible()
    expect(page.get_by_text("0 products found for 'hXwrglzd'")).to_be_visible()
    expect(page.get_by_text("There are no products found.")).to_be_visible()

def test_catalogo_filtro_categoria(page):
    paginacatalogo = PaginaCatalogo(page)
    paginacatalogo.acessar_home()
    paginacatalogo.filtrar_por_categoria("Hammer")
    page.wait_for_timeout(2000)
    quantidade = paginacatalogo.card_produto.count()
    print(f'Quantidade: {quantidade}')
    quantidade_martelos = paginacatalogo.card_produto.get_by_text("Hammer").count()
    assert quantidade == quantidade_martelos, "Quantidade de cards não é igual a quantidade de cards com martelo"
    assert quantidade > 0

def test_catalogo_filtro_preco(page):
    paginacatalogo = PaginaCatalogo(page)
    paginacatalogo.acessar_home()
    paginacatalogo.select_ordem.select_option("price,asc")
    page.wait_for_timeout(2000)
    prod_preco = paginacatalogo.card_preco.all_text_contents()
    print(prod_preco)
    valores = [float(preco.replace('$', '')) for preco in prod_preco]
    print(valores)
    for i in range(len(valores) - 1):
        if valores[i] > valores[i + 1]:
            assert False, "A lista não está em ordem crescente"

def teste_catalogo_consistencia(page):
    paginacatalogo = PaginaCatalogo(page)
    paginacatalogo.acessar_home()
    page.pause()
    produto_nome = paginacatalogo.card_produto.locator('[data-test="product-name"]').first.text_content()
    produto_preco = paginacatalogo.card_preco.first.text_content()
    paginacatalogo.card_produto.first.click()
    page.wait_for_timeout(2000)
    print(produto_nome)
    print(produto_preco)
    expect(page.get_by_text(produto_nome).first).to_be_visible()
    expect(page.get_by_text(produto_preco)).to_be_visible()



    page.pause()