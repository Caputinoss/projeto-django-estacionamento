# 🚗 Parking Service API — Sistema de Estacionamento com Django REST

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0-green.svg)
![DRF](https://img.shields.io/badge/DRF-API-red.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

> Projeto construído com **Django REST Framework** durante a live [py_live #039 — Sistema e API de Estacionamento com Python e Django do Zero (Parte 1)](https://pickle-reading-bd9.notion.site/py_live-042-1cd9956f3dc9802387c6ddd312693423), com o objetivo de criar uma **API completa e escalável para gestão de estacionamentos.**

---

## 🧠 Visão Geral

O **Parking Service API** é um sistema backend que oferece funcionalidades completas para controle de **clientes, veículos, vagas e tickets de estacionamento**, com administração via painel interno e endpoints RESTful para futuras integrações.

🗺️ **Documentação de referência:**  
[Whimsical — Diagrama do Sistema Parking Service](https://whimsical.com/parking-service-SSoifu29a1MVLAmLAPMk2a)
[Notion — Sistema e API de Estacionamento (By: pycodebr)](https://pickle-reading-bd9.notion.site/py_live-039-1bf9956f3dc9804998aaee8c46f77751)

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|-------------|-------------|
| **Python 3.11+** | Linguagem principal |
| **Django 5+** | Framework web |
| **Django REST Framework (DRF)** | Criação da API RESTful |
| **SQLite** | Banco de dados local |
| **PostgreSQL** *(futuro)* | Banco para produção |
| **JWT (SimpleJWT)** | Autenticação e segurança |
| **Jazzmin** | Dashboard administrativo moderno |

---

## 🧩 Estrutura do Projeto
projeto-django-estacionamento/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── core/ # Configurações principais do projeto
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── parking/ # App principal
│ ├── models.py # Entidades: Cliente, Veículo, Vaga, Ticket
│ ├── serializers.py # Serialização dos dados para API
│ ├── views.py # Lógica dos endpoints
│ ├── urls.py # Rotas da aplicação
│ ├── signals.py # Atualização automática de status das vagas
│ ├── admin.py # Configuração do Django Admin
│ ├── permissions.py # Regras de acesso e autenticação
│ ├── tests.py # Testes automatizados
│ └── services/ # Serviços auxiliares (futuro: notificações, Celery)
│
└── docs/
└── README.md # Este arquivo


---

## 🧮 Modelagem de Domínio

| Entidade | Descrição |
|-----------|------------|
| **Cliente** | Representa o usuário proprietário dos veículos |
| **Veículo** | Armazena dados como placa, modelo e cliente associado |
| **Vaga** | Representa o espaço físico disponível no estacionamento |
| **Ticket** | Registra a entrada, saída e valor cobrado |
| **Usuário (Admin)** | Controle de acessos e permissões no sistema interno |

---

## 🚀 Funcionalidades Implementadas

### ✅ Funcionais
- Sistema de administração interno (Django Admin + Jazzmin)
- Cadastros de:
  - Clientes  
  - Veículos  
  - Vagas  
  - Entradas e saídas (tickets)
- Status de vagas automático (via *signals*)
- API RESTful para todas as entidades
- Autenticação via JWT Token
- Filtros dinâmicos (via **DjangoFilterBackend**)
- Documentação Swagger/OpenAPI (via **drf-yasg**)

## 🧰 Como Executar o Projeto Localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Caputinoss/projeto-django-estacionamento.git
cd projeto-django-estacionamento

###  2️⃣ Criar, ativar o ambiente virtual e instalar dependências
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt

### 3️⃣ Aplicar as migrações e criar superusuário

python manage.py migrate
python manage.py createsuperuser

### 4️⃣ Rodar o Servidor local
python manage.py runserver

## 📡 Swagger
- Painel Admin → http://localhost:8000/admin/
- Swagger API Docs → http://localhost:8000/api/v1/docs/
