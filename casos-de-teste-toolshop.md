# 🎫 Tarefa: Automação de Testes E2E — Toolshop (practicesoftwaretesting.com)

**Tipo:** Automação de Testes E2E
**Aplicação:** Toolshop — e-commerce de demonstração
**Ambiente:** https://practicesoftwaretesting.com
**Solicitante:** P.O. / Time de Produto

## Contexto

Precisamos de cobertura automatizada de ponta a ponta para a jornada completa de compra no Toolshop: cadastro, login, navegação no catálogo, carrinho e checkout. O objetivo é ter uma suíte confiável, rodando em pipeline de CI a cada push, que sirva de rede de segurança para futuras mudanças na aplicação.

## User Stories

**US01 — Cadastro**
> Como visitante, quero criar uma conta para poder fazer compras e acompanhar meus pedidos.

**US02 — Login**
> Como usuário cadastrado, quero fazer login com meu email e senha para acessar minha conta.

**US03 — Busca e navegação no catálogo**
> Como visitante, quero buscar, filtrar e ordenar produtos para encontrar o que procuro rapidamente.

**US04 — Carrinho de compras**
> Como usuário, quero adicionar, atualizar e remover produtos do carrinho para montar meu pedido antes de finalizar a compra.

**US05 — Checkout**
> Como usuário com itens no carrinho, quero concluir a compra informando endereço e pagamento, para receber a confirmação do pedido.

---

## Casos de Teste

### Cadastro

| ID | Título | Pré-condição | Passos | Resultado esperado | Prioridade |
|----|--------|--------------|--------|---------------------|------------|
| CAD-01 | Cadastro com dados válidos | Email ainda não usado | 1. Acessar página de cadastro<br>2. Preencher todos os campos obrigatórios com dados válidos<br>3. Enviar formulário | Conta criada; usuário é redirecionado para login ou área logada | Alta |
| CAD-02 | Cadastro com email já existente | Email já cadastrado previamente | 1. Acessar página de cadastro<br>2. Preencher com um email já usado<br>3. Enviar formulário | Mensagem de erro informando que o email já está em uso | Alta |
| CAD-03 | Cadastro com campos obrigatórios vazios | — | 1. Acessar página de cadastro<br>2. Deixar campos obrigatórios em branco<br>3. Tentar enviar | Validação de campo obrigatório é exibida; formulário não é enviado | Média |

### Login

| ID | Título | Pré-condição | Passos | Resultado esperado | Prioridade |
|----|--------|--------------|--------|---------------------|------------|
| LOGIN-01 | Login com credenciais válidas | Usuário cadastrado existe | 1. Acessar página de login<br>2. Preencher email e senha válidos<br>3. Clicar em "Entrar" | Usuário é redirecionado para a área logada (conta/perfil) | Alta |
| LOGIN-02 | Login com senha incorreta | Usuário cadastrado existe | 1. Acessar página de login<br>2. Preencher email válido e senha incorreta<br>3. Clicar em "Entrar" | Mensagem de erro é exibida; usuário permanece na tela de login | Alta |
| LOGIN-03 | Login com email não cadastrado | — | 1. Acessar página de login<br>2. Preencher email inexistente e qualquer senha<br>3. Clicar em "Entrar" | Mensagem de erro é exibida | Alta |
| LOGIN-04 | Tentativa de login com campos vazios | — | 1. Acessar página de login<br>2. Deixar email e senha em branco<br>3. Clicar em "Entrar" | Validação de campo obrigatório é exibida; nenhuma requisição de login é enviada | Média |

### Catálogo

| ID | Título | Pré-condição | Passos | Resultado esperado | Prioridade |
|----|--------|--------------|--------|---------------------|------------|
| CAT-01 | Busca por produto existente | — | 1. Acessar a home<br>2. Buscar por um produto existente (ex: "hammer")<br>3. Confirmar busca | Ao menos um produto correspondente é exibido na listagem | Alta |
| CAT-02 | Busca por produto inexistente | — | 1. Acessar a home<br>2. Buscar por um termo inexistente (ex: "xyznotfound")<br>3. Confirmar busca | Mensagem de "nenhum resultado encontrado" é exibida; nenhum produto listado | Alta |
| CAT-03 | Filtro por categoria | Catálogo possui múltiplas categorias | 1. Acessar a home<br>2. Selecionar uma categoria no filtro | Todos os produtos exibidos pertencem à categoria selecionada (a listagem não exibe a categoria de cada produto, então a verificação usa uma categoria cujo nome aparece no nome dos produtos, ex: "Hammer") | Média |
| CAT-04 | Ordenação por preço | Catálogo possui múltiplos produtos | 1. Acessar a home<br>2. Selecionar ordenação "menor preço" | Produtos exibidos em ordem crescente de preço | Média |
| CAT-05 | Consistência entre listagem e detalhe do produto | Catálogo possui ao menos 1 produto | 1. Abrir a listagem de produtos<br>2. Anotar nome e preço de um produto<br>3. Clicar no produto para abrir o detalhe | Nome e preço na página de detalhe correspondem aos exibidos na listagem | Média |

### Carrinho

| ID | Título | Pré-condição | Passos | Resultado esperado | Prioridade |
|----|--------|--------------|--------|---------------------|------------|
| CART-01 | Adicionar produto ao carrinho | Produto disponível no catálogo | 1. Abrir um produto<br>2. Clicar em "Adicionar ao carrinho" | Item aparece no carrinho com quantidade 1 | Alta |
| CART-02 | Adicionar o mesmo produto duas vezes | Produto já está no carrinho | 1. Adicionar um produto ao carrinho<br>2. Adicionar o mesmo produto novamente | Quantidade do item soma para 2; não cria linha duplicada | Alta |
| CART-03 | Atualizar quantidade de um item | Item já está no carrinho | 1. Abrir o carrinho<br>2. Alterar a quantidade de um item para um novo valor | Total do carrinho é recalculado corretamente com base na nova quantidade | Alta |
| CART-04 | Remover item do carrinho | Item já está no carrinho | 1. Abrir o carrinho<br>2. Clicar em remover em um item | Item desaparece da lista; total é recalculado | Alta |
| CART-05 | Estado de carrinho vazio | Carrinho sem itens | 1. Acessar o carrinho sem ter adicionado produtos | Nenhum item, total ou botão de avançar é exibido; nenhum erro ou tela em branco (o restante do layout continua normal). Nota: comportamento real observado — a aplicação não exibe uma mensagem de "carrinho vazio" ao carregar a página já vazia, apenas quando o último item é removido interativamente | Baixa |

### Checkout

| ID | Título | Pré-condição | Passos | Resultado esperado | Prioridade |
|----|--------|--------------|--------|---------------------|------------|
| CHK-01 | Checkout completo com sucesso (usuário logado) | Usuário logado com item no carrinho | 1. Ir para o carrinho<br>2. Prosseguir para checkout<br>3. Preencher endereço de entrega<br>4. Preencher forma de pagamento<br>5. Confirmar pedido | Página de confirmação exibida com número/resumo do pedido | Alta |
| CHK-02 | Checkout sem itens no carrinho | Carrinho vazio, usuário logado | 1. Tentar acessar checkout diretamente | Usuário é bloqueado: não é exibido nenhum item, total ou botão de avançar (não há mensagem nem redirecionamento) | Alta |
| CHK-03 | Checkout com endereço incompleto | Usuário logado com item no carrinho | 1. Ir para o carrinho<br>2. Prosseguir para checkout<br>3. Deixar campo obrigatório de endereço vazio<br>4. Tentar avançar | Validação de campo obrigatório é exibida; checkout não avança | Média |
| CHK-04 | Checkout sem estar logado | Item no carrinho, usuário deslogado | 1. Adicionar item ao carrinho sem login<br>2. Tentar prosseguir para checkout | Usuário é direcionado para login/cadastro antes de finalizar | Média |
| CHK-05 | Resumo do pedido reflete os itens do carrinho | Usuário logado com 2+ itens distintos no carrinho | 1. Ir até a etapa de resumo do checkout | Itens, quantidades e total no resumo correspondem exatamente ao carrinho | Alta |

---

## Critérios de aceite gerais

- Todos os testes rodam via `pytest` sem intervenção manual, localmente e em CI.
- Testes seguem o padrão Page Object Model, com classes em `pages/` herdando de `BasePage`.
- Nomes de classes, métodos e variáveis de Page Object em português.
- Nenhum teste depende da ordem de execução dos demais (isolamento) — cada teste cria seu próprio estado (ex: usuário novo via massa de dados dinâmica quando aplicável).
- Testes negativos (CAD-02, CAD-03, LOGIN-02, LOGIN-03, LOGIN-04, CAT-02, CHK-02, CHK-03) validam explicitamente a mensagem/comportamento de erro, nunca dependem apenas de timeout.
- Testes marcados com `@pytest.mark.smoke` cobrem o caminho feliz de cada fluxo (CAD-01, LOGIN-01, CAT-01, CART-01, CHK-01) para rodar rápido em CI a cada push.
- Pipeline de CI (GitHub Actions) executa a suíte completa e publica relatório de execução como artefato.
- README do repositório documenta: objetivo do projeto, stack, como rodar localmente, como rodar em CI, estrutura de pastas.
