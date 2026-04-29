
---

## 🗄️ Estrutura do Banco de Dados

### Tabela: categories

- id (PK)
- name (string)
- created_at
- updated_at

### Tabela: transactions

- id (PK)
- category_id (FK)
- description (string)
- type (income | expense)
- amount (decimal)
- transaction_date (date)
- created_at
- updated_at

---

## 🔗 Endpoints

### Categorias

- GET /categories
- POST /categories
- GET /categories/{id}
- PUT /categories/{id}
- DELETE /categories/{id}

### Transações

- GET /transactions
- POST /transactions
- GET /transactions/{id}
- PUT /transactions/{id}
- DELETE /transactions/{id}

### Dashboard

- GET /dashboard/summary
- GET /dashboard/by-category

---

## 📌 Possíveis Evoluções

- Autenticação com JWT
- Multiusuário
- Integração com APIs bancárias
- Exportação de relatórios (CSV/PDF)
- Dashboard com gráficos
- Integração com WhatsApp para alertas

---

## 💡 Nome do Projeto

- MiniFinance API
- Clokfin Lite
- MyWallet API

---

## ▶️ Como Rodar o Projeto

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar aplicação
uvicorn app.main:app --reload