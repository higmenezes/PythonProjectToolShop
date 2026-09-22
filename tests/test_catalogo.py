from pages.pagina_catalogo import PaginaCatalogo
from playwright.sync_api import expect

def test_catalogo_busca_produto_existente(page):
    paginacatalogo = PaginaCatalogo(page)
    paginacatalogo.acessar_home()
    paginacatalogo.input_busca.fill("hammer")
    paginacatalogo.botao_busca.click()
    expect(page.get_by_text("Searched for: hammer")).to_be_visible()
    page.pause()
    quantidade = paginacatalogo.card_produto.count()
    assert quantidade > 0, f'Quantidade não é maior que zero'
    print(f'Quantidade: {quantidade}')
    page.pause()

def test_catalogo_busca_termo_inexistente(page):
    paginacatalogo = PaginaCatalogo(page)
    paginacatalogo.acessar_home()
    paginacatalogo.input_busca.fill("hXwrglzd")
    paginacatalogo.botao_busca.click()
    expect(page.get_by_text("Searched for: hXwrglzd")).to_be_visible()
    expect(page.get_by_text("0 products found for 'hXwrglzd'")).to_be_visible()
    expect(page.get_by_text("There are no products found.")).to_be_visible()

def test_catalogo_filtro_categoria(page):
    paginacatalogo = PaginaCatalogo(page)
    paginacatalogo.acessar_home()
    page.locator("#filters").get_by_text("Hammer").click()
    '''como validar qualquer aparição da palavra Hammer'''
    '''fazer validação de categoria completa e não só hammer - buscar como validar várias palavras diferentes'''
    expect(page.get_by_text("Hammer")).to_be_visible()

def test_catalogo_filtro_preco(page):
    paginacatalogo = PaginaCatalogo(page)
    paginacatalogo.acessar_home()
    paginacatalogo.select_ordem.select_option("price,asc")
    '''Como validar que os preços estão do menor pro maior'''
    page.pause()