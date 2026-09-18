

class PaginaCadastro():
    def __init__(self, page):
        self.page = page
        self.input_primeiro_nome = page.get_by_placeholder("First name *")
        self.input_sobrenome = page.get_by_placeholder("Your last name *")
        self.input_data_nascimento = page.get_by_placeholder("YYYY-MM-DD")
        self.select_pais = page.locator('[data-test="country"]')
        self.input_cep = page.get_by_placeholder("Your Postcode *")
        self.input_numero_casa = page.get_by_placeholder("e.g. 42 *")
        self.input_rua = page.get_by_placeholder("Your Street *")
        self.input_cidade = page.get_by_placeholder("Your City *")
        self.input_estado = page.get_by_placeholder("Your State *")
        self.input_telefone = page.get_by_placeholder("Your phone *")
        self.input_email = page.get_by_placeholder("Your email *")
        self.input_senha = page.get_by_placeholder("Your password")
        self.botao_cadastrar = page.get_by_role("button", name="Register")
        self.alerta_erro_cadastro = page.locator('[data-test="register-error"]')

    def acessar_cadastro(self):
        self.page.goto("/auth/register")

    def preencher_cadastro(self, primeiro_nome=None, ultimo_nome=None, data_nascimento=None,
                           pais=None, cep=None, numero_casa=None, rua=None, cidade=None, estado=None,
                           telefone=None, email=None, senha=None):
        if primeiro_nome:
            self.input_primeiro_nome.fill(primeiro_nome)
        if ultimo_nome:
            self.input_sobrenome.fill(ultimo_nome)
        if data_nascimento:
            self.input_data_nascimento.fill(data_nascimento)
        if pais:
            self.select_pais.select_option(pais)
        if pais:
            self.input_cep.fill(cep)
        if numero_casa:
            self.input_numero_casa.fill(numero_casa)
        if rua:
            self.input_rua.fill(rua)
        if cidade:
            self.input_cidade.fill(cidade)
        if estado:
            self.input_estado.fill(estado)
        if telefone:
            self.input_telefone.fill(telefone)
        if email:
            self.input_email.fill(email)
        if senha:
            self.input_senha.fill(senha)
