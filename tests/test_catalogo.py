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