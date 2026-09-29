from pages.pagina_carrinho import PaginaCarrinho

class PaginaCheckout(PaginaCarrinho):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.botao_prosseguir_checkout = page.locator("[data-test=\"proceed-1\"]")
        self.botao_confirmar_login_checkout = page.locator("[data-test=\"proceed-2\"]")
        self.botao_prosseguir_endereco = page.locator("[data-test=\"proceed-3\"]")
        self.input_email_checkout = page.locator("[data-test=\"email\"]")
        self.input_senha_checkout = page.locator("[data-test=\"password\"]")
        self.botao_login_checkout = page.locator("[data-test=\"login-submit\"]")
        self.link_cadastro_checkout = page.locator("[data-test=\"register-link\"]")
        self.select_pais_endereco = page.locator("[data-test=\"country\"]")
        self.input_cep_endereco = page.locator("[data-test=\"postal_code\"]")
        self.input_numero_endereco = page.locator("[data-test=\"house_number\"]")
        self.input_rua_endereco = page.locator("[data-test=\"street\"]")
        self.input_cidade_endereco = page.locator("[data-test=\"city\"]")
        self.input_estado_endereco = page.locator("[data-test=\"state\"]")
        self.select_forma_pagamento = page.locator("[data-test=\"payment-method\"]")
        self.botao_finalizar_pagamento = page.locator("[data-test=\"finish\"]")
        self.texto_pagamento_sucesso = page.locator("[data-test=\"payment-success-message\"]")

    def prosseguir_para_checkout(self):
        self.botao_prosseguir_checkout.click()
        self.page.wait_for_timeout(1000)

    def confirmar_login_no_checkout(self):
        self.botao_confirmar_login_checkout.click()
        self.page.wait_for_timeout(1000)

    def preencher_endereco_entrega(self, pais, cep, numero_casa, rua, cidade, estado):
        if pais:
            self.select_pais_endereco.select_option(label=pais)
        if cep:
            self.input_cep_endereco.fill(cep)
        if numero_casa:
            self.input_numero_endereco.fill(numero_casa)
        if rua:
            self.input_rua_endereco.fill(rua)
        if cidade:
            self.input_cidade_endereco.fill(cidade)
        if estado:
            self.input_estado_endereco.fill(estado)
        self.page.wait_for_timeout(500)

    def prosseguir_para_pagamento(self):
        self.botao_prosseguir_endereco.click()
        self.page.wait_for_timeout(1000)

    def selecionar_forma_pagamento(self, forma):
        self.select_forma_pagamento.select_option(label=forma)
        self.page.wait_for_timeout(500)

    def finalizar_pedido(self):
        self.botao_finalizar_pagamento.click()
        self.page.wait_for_timeout(1500)
