

class PaginaCatalogo():
    def __init__(self, page):
        self.page = page
        self.input_busca = page.locator("[data-test=\"search-query\"]")
        self.botao_busca = page.locator("[data-test=\"search-submit\"]")
        self.card_produto = page.locator('[data-test^="product-"]:visible .card-body')
        self.card_preco = page.locator('[data-test^="product-"]:visible .card-footer').locator("[data-test='product-price']")
        self.select_ordem = page.locator("[data-test=\"sort\"]")

    def acessar_home(self):
        self.page.goto("")
        self.page.wait_for_timeout(1000)

    def buscar_produto(self, prod_search):
        self.input_busca.fill(prod_search)
        self.botao_busca.click()
        self.page.wait_for_timeout(1000)

    def filtrar_por_categoria(self, categ_search):
        self.page.get_by_role("checkbox", name=categ_search).check()