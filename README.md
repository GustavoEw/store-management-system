# Sistema de Gestão – Coisas Fits

Sistema de gestão desenvolvido em Python para auxiliar no controle operacional da loja **Coisas Fits**, com integração ao Google Sheets para armazenamento e gerenciamento de dados.

## 🚀 Objetivo

Desenvolver uma aplicação simples e funcional que permita organizar as informações da loja, começando pelo cadastro e gerenciamento de produtos.

O projeto será desenvolvido gradualmente, priorizando primeiro as funcionalidades essenciais.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **gspread:** biblioteca utilizada para integração com o Google Sheets.
- **Google Service Account:** autenticação para acesso à planilha.
- **Google Sheets:** armazenamento inicial dos dados.

## 📂 Estrutura do projeto

A estrutura será organizada conforme o desenvolvimento da aplicação.

```text
Caixa/
├── main.py
├── product.py
└── __pycache__/
```

> A estrutura poderá ser ampliada conforme novos módulos forem implementados.

## 📦 Gerenciamento de produtos

O projeto já possui uma classe `Product`, responsável por representar os produtos e organizar seus atributos.

Informações atualmente contempladas:

- ID do produto;
- Nome;
- Preço;
- Quantidade em estoque.

A classe possui métodos para definir e recuperar os dados do produto.

### Teste de criação de produtos

Atualmente, existe uma função de teste pelo terminal que coleta as informações do produto e retorna os valores para preenchimento do objeto.

## ☁️ Integração com Google Sheets

A autenticação com o Google Sheets utilizando uma Service Account já foi configurada.

A planilha exclusiva do projeto também já foi acessada por meio da conta de serviço.

**Próxima etapa:** implementar a inserção e edição de produtos diretamente na planilha.

## 📌 Desenvolvimento

O desenvolvimento seguirá estas etapas:

- [x] Configuração do ambiente Python.
- [x] Configuração da autenticação com Google Service Account.
- [x] Acesso à planilha pelo `gspread`.
- [x] Criação da classe `Product`.
- [x] Implementação dos métodos de cadastro e recuperação de dados.
- [x] Teste de criação de produtos pelo terminal.
- [ ] Inserção de produtos no Google Sheets.
- [ ] Edição de produtos existentes.
- [ ] Validação dos dados de entrada.
- [ ] Desenvolvimento de uma interface gráfica.

## 📖 Filosofia do projeto

O objetivo é construir um sistema funcional, simples e de fácil manutenção.

A implementação seguirá a abordagem:

**Fazer funcionar primeiro. Depois melhorar e automatizar.**

Novas funcionalidades serão adicionadas conforme as necessidades reais da loja.
