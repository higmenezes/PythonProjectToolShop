# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Playwright + pytest E2E test suite for **Toolshop** (https://practicesoftwaretesting.com), a public demo e-commerce app. There is no application source code here — this repo only contains browser automation tests that exercise the live site. The full spec (user stories, test case tables, acceptance criteria) lives in `casos-de-teste-toolshop.md`, in Portuguese.

## Commands

Activate the venv first (Windows):
```
.venv\Scripts\activate
```

Run the full suite:
```
pytest
```

Run one file / one test:
```
pytest tests/test_login.py
pytest tests/test_login.py::test_pagina_login_senha_incorreta
```

Dependencies are pinned in `requirements.txt` (install with `pip install -r requirements.txt`, then `python -m playwright install chromium`). There is no lint config.

Browsers run **headed** by default; set `HEADLESS=true` to run headless (PowerShell: `$env:HEADLESS="true"; pytest`). The `navegador` fixture in `conftest.py` reads this variable.

CI: `.github/workflows/testes.yml` runs the suite headless on Ubuntu on push/PR to `master` and via manual dispatch (`workflow_dispatch`), uploading `relatorio/junit.xml` as an artifact. Don't commit `page.pause()` calls — they hang the CI job; use `PWDEBUG=1` locally to debug instead.

## Architecture

**Page Object Model**, per the spec in `casos-de-teste-toolshop.md`: one class per page in `pages/`, one test module per feature in `tests/`, all naming in Portuguese (page objects, methods, variables). There is currently no shared `BasePage` — each page class is a standalone `__init__(self, page)` that stores locators as attributes.

- `conftest.py` — session-scoped `navegador` fixture launches one Chromium browser for the whole run; function-scoped `page` fixture creates a fresh `BrowserContext` per test (via `base_url="https://practicesoftwaretesting.com/"`) so tests don't share cookies/session state, then tears it down. `page.goto("")` / `page.goto("/auth/login")` in page objects rely on this base URL.
- `pages/pagina_catalogo.py` — `PaginaCatalogo` is the base for catalog/search/sort locators (`acessar_home`, `buscar_produto`, `filtrar_por_categoria`).
- `pages/pagina_carrinho.py` — `PaginaCarrinho` **extends `PaginaCatalogo`** (cart flows start from a product card in the catalog), adding add-to-cart and cart-total locators. `acessar_carrinho()` navigates to `checkout` (the cart page shares the checkout route on this app).
- `pages/pagina_login.py`, `pages/pagina_cadastro.py` — standalone, no inheritance.
- Locators mix `data-test` attributes (`page.locator('[data-test="..."]')`), placeholder text, and role-based queries — match whichever style the target page object already uses when adding new locators to it.

Tests assert against literal English UI strings/messages from the live site (e.g. `"Product added to shopping cart."`, `"Invalid email or password"`) since there's no backend/mocking layer — these are real assertions against production text, so if the site copy changes, tests need to be updated to match.

Known state coupling to watch for: `test_login.py` and `test_cadastro.py` assume a specific account (`higtest22@test.com`) already exists on the live site (created by `test_cadastro_com_dados_validos`) — these aren't currently isolated per the spec's stated goal of dynamic/independent test data, despite `casos-de-teste-toolshop.md` calling for exactly that. Don't assume login tests will pass standalone against a clean environment.

## Conventions from the spec (`casos-de-teste-toolshop.md`)

- New page objects/methods/tests: name everything in Portuguese, following existing files.
- Negative-path tests (invalid email, empty fields, no results, etc.) must assert on the actual error message/behavior shown, not just rely on a timeout.
- Smoke-path tests are tagged `@pytest.mark.smoke` (not yet configured as a marker or applied to any test — add `markers = smoke: ...` to a pytest config file if you introduce this).
