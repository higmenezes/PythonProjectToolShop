

class PaginaLogin():
    def __init__(self, page):
        self.page = page
        self.input_email_login = page.locator("[data-test=\"email\"]")
        self.input_senha_login = page.locator("[data-test=\"password\"]")
        self.botao_login = page.locator("[data-test=\"login-submit\"]")

    def acessar_login(self):
        self.page.goto("/auth/login")

    def preencher_login(self, email, senha):
        self.input_email_login.fill(email)
        self.input_senha_login.fill(senha)