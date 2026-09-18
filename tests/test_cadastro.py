from pages.pagina_cadastro import PaginaCadastro
from playwright.sync_api import expect


def test_cadastro_com_dados_validos(page):
    paginacadastro = PaginaCadastro(page)
    paginacadastro.acessar_cadastro()
    paginacadastro.preencher_cadastro(primeiro_nome='Higtest', ultimo_nome='Testing', data_nascimento='2000-06-25',
                                      pais='Brazil', cep='1234567', numero_casa='124', rua='Avenida Atlântica',
                                      cidade='Rio de Janeiro',
                                      estado='RJ', telefone='21567846845', email='higtest22@test.com', senha='1HgJx2d45#')
    paginacadastro.botao_cadastrar.click()
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    page.pause()

def test_cadastro_com_email_ja_existente(page):
    paginacadastro = PaginaCadastro(page)
    paginacadastro.acessar_cadastro()
    paginacadastro.preencher_cadastro(primeiro_nome='Higtest', ultimo_nome='Testing', data_nascimento='2000-06-25',
                                      pais='Brazil', cep='1234567', numero_casa='124', rua='Avenida Atlântica',
                                      cidade='Rio de Janeiro',
                                      estado='RJ', telefone='21567846845', email='higtest@test.com', senha='1HgJxd45#')
    paginacadastro.botao_cadastrar.click()
    expect(page.get_by_text("A customer with this email address already exists.")).to_be_visible()

def test_cadastro_com_campos_obrigatorios_vazios(page):
    paginacadastro = PaginaCadastro(page)
    paginacadastro.acessar_cadastro()
    paginacadastro.preencher_cadastro(primeiro_nome='Higtest')
    paginacadastro.botao_cadastrar.click()
    expect(page.get_by_text("Phone is required.")).to_be_visible()
    page.pause()