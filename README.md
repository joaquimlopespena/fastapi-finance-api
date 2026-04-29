# 📌 MiniFinance API

API REST desenvolvida com **Python + FastAPI** para gerenciamento de gastos pessoais, permitindo o controle de receitas, despesas e categorização financeira de forma simples e eficiente.

O objetivo do projeto é servir como base prática para estudo de desenvolvimento backend moderno, utilizando boas práticas de arquitetura, organização de código e integração com banco de dados relacional (**MySQL**).

---

## 🚀 Funcionalidades

### 📂 Gestão de Categorias
- Criar categoria
- Listar categorias
- Atualizar categoria
- Excluir categoria
- Organização de gastos por tipo (ex: Alimentação, Transporte, Lazer)

### 💰 Gestão de Transações
- Registro de **receitas** e **despesas**
- Associação com categorias
- Listagem de transações
- Filtros por período
- Filtro por tipo (entrada/saída)

### 📊 Dashboard Financeiro
- Total de receitas
- Total de despesas
- Saldo atual
- Gastos agrupados por categoria

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12+
- FastAPI
- SQLAlchemy 2.0
- MySQL
- Pydantic
- Uvicorn
- Docker (opcional)

---

## 🧠 Objetivo do Projeto

Este projeto tem como foco:

- Praticar desenvolvimento de APIs REST com FastAPI
- Trabalhar com ORM (SQLAlchemy)
- Aplicar validações com Pydantic
- Implementar um CRUD completo
- Criar consultas com filtros e agregações
- Organizar o projeto em camadas (models, schemas, services, repositories)
- Simular um cenário real de backend financeiro

---

## 📁 Estrutura do Projeto

app/
├── core/ # Configurações (database, settings)
├── models/ # Modelos do banco (SQLAlchemy)
├── schemas/ # Validação (Pydantic)
├── repositories/ # Acesso ao banco
├── services/ # Regras de negócio
├── routes/ # Endpoints da API
└── main.py # Inicialização da aplicação
