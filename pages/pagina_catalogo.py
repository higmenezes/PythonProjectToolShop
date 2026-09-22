

class PaginaCatalogo():
    def __init__(self, page):
        self.page = page
        self.input_busca = page.locator("[data-test=\"search-query\"]")
        self.botao_busca = page.locator("[data-test=\"search-submit\"]")
        self.card_produto = page.locator('[data-test^="product-"]:visible .card-body')
        self.select_ordem = page.locator("[data-test=\"sort\"]")


    def acessar_home(self):
        self.page.goto("")