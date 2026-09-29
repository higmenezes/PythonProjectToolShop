from pages.pagina_catalogo import PaginaCatalogo

class PaginaCarrinho(PaginaCatalogo):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.adicionar_carrinho = page.locator("[data-test=\"add-to-cart\"]")
        self.campo_cart_quantity = page.locator("[data-test=\"product-quantity\"]")
        self.texto_total_produto = page.locator("[data-test=\"line-price\"]")
        self.texto_total_carrinho = page.locator("[data-test=\"cart-total\"]")
        self.texto_preco_produto = page.locator("[data-test=\"product-price\"]")


    def acessar_carrinho(self):
        self.page.goto("checkout")
        self.page.wait_for_timeout(1000)