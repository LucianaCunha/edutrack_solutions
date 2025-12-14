# EduTrack Solutions

Sistema de gerenciamento educacional desenvolvido com Django REST Framework para controle de professores, turmas e alunos.

## Instituições de Fomento e Parceria
[![Website IFB](https://img.shields.io/badge/Website-IFB-%23508C3C.svg?labelColor=%23C8102E)](https://www.ifb.edu.br/) 
[![Website ihwbr](https://img.shields.io/badge/Website-ihwbr-%23DAA520.svg?labelColor=%232E2E2E)](https://hardware.org.br/)

## Orientador (link para o perfil do orientador)

[![LinkedIn Claudio Ulisse](https://img.shields.io/badge/LinkedIn-Claudio_Ulisse-%230077B5.svg?labelColor=%23FFFFFF&logo=linkedin)](https://www.linkedin.com/in/claudioulisse/)
[![GitHub claulis](https://img.shields.io/badge/GitHub-claulis_(Claudio_Ulisse)-%23181717.svg?logo=github&logoColor=white)](https://github.com/claulis)
[![Lattes Claudio Ulisse](https://img.shields.io/badge/Lattes-Claudio_Ulisse-green.svg?logo=cnpq&logoColor=white)](http://lattes.cnpq.br/4607303092740768)

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Instalação](#instalação)
- [Uso](#uso)
- [Endpoints da API](#endpoints-da-api)
- [Modelos de Dados](#modelos-de-dados)
- [Autenticação](#autenticação)
- [Exemplos de Requisições](#exemplos-de-requisições)
- [Licença](#licença)


## 🎯 Sobre o Projeto

EduTrack Solutions é uma API RESTful completa para gerenciamento de ambientes educacionais. O sistema permite o controle de professores, turmas e alunos, incluindo funcionalidades de matrícula, relacionamentos entre entidades e gestão de dados acadêmicos.


## ✨ Funcionalidades

### Gestão de Professores
- ✅ CRUD completo de professores
- ✅ Associação de professores a departamentos
- ✅ Controle de status ativo/inativo
- ✅ Listagem de turmas por professor

### Gestão de Turmas
- ✅ CRUD completo de turmas
- ✅ Associação de turmas a professores
- ✅ Controle de datas de início e fim
- ✅ Gestão de status (Ativa, Concluída, Cancelada)
- ✅ Listagem de alunos matriculados

### Gestão de Alunos
- ✅ CRUD completo de alunos
- ✅ Matrícula em múltiplas turmas
- ✅ Desmatrícula de turmas
- ✅ Controle de dados pessoais e acadêmicos
- ✅ Histórico de matrículas

### Funcionalidades Avançadas
- 🔐 Autenticação via Token e Session
- 📄 Paginação automática (10 itens por página)
- 🔍 Filtros e buscas
- 📊 Relacionamentos complexos (1:N e N:N)
- 🛡️ Permissões baseadas em autenticação

## 🚀 Tecnologias Utilizadas

### Backend
- **Python 3.10** - Linguagem de programação
- **Django 4.2** - Framework web
- **Django REST Framework 3.14.0** - Construção da API REST
- **SQLite** - Banco de dados (desenvolvimento)

### Ferramentas de Desenvolvimento
- **VS Code** - IDE recomendada
- **Dev Containers** - Ambiente de desenvolvimento containerizado
- **Git** - Controle de versão

## 🏗️ Arquitetura do Sistema

### Estrutura de Diretórios

```
edutrack_solutions/
│
├── .devcontainer/
│   └── devcontainer.json          # Configuração do ambiente de desenvolvimento
│
├── myproject/
│   ├── core/                      # Aplicativo principal
│   │   ├── migrations/            # Migrações do banco de dados
│   │   ├── admin.py              # Configuração do Django Admin
│   │   ├── apps.py               # Configuração do app
│   │   ├── models.py             # Modelos de dados
│   │   ├── serializers.py        # Serializers da API
│   │   ├── views.py              # Views e ViewSets
│   │   ├── urls.py               # Rotas da API
│   │   └── tests.py              # Testes unitários
│   │
│   ├── myproject/                 # Configurações do projeto
│   │   ├── __init__.py
│   │   ├── settings.py           # Configurações gerais
│   │   ├── urls.py               # Rotas principais
│   │   ├── wsgi.py               # WSGI config
│   │   └── asgi.py               # ASGI config
│   │
│   ├── manage.py                  # Utilitário de linha de comando
│   └── requirements.txt           # Dependências do projeto
│
├── .gitignore
└── README.md
```

### Diagrama de Relacionamentos

```
┌─────────────┐         1:N         ┌─────────────┐         N:N         ┌─────────────┐
│  Professor  │────────────────────▶│    Turma    │◀────────────────────│    Aluno    │
└─────────────┘                     └─────────────┘                     └─────────────┘
```

## 📦 Instalação

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/edutrack_solutions.git
cd edutrack_solutions
```

2. **Crie e ative o ambiente virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
cd myproject
pip install -r requirements.txt
```

4. **Execute as migrações**
```bash
python manage.py migrate
```

5. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

6. **Inicie o servidor de desenvolvimento**
```bash
python manage.py runserver
```

A API estará disponível em: `http://localhost:8000/api/`


## 💻 Uso

### Acessando o Admin

Acesse `http://localhost:8000/admin/` e faça login com as credenciais do superusuário criado.

### Acessando a API

A API está disponível em `http://localhost:8000/api/` com os seguintes endpoints base:
- `/api/professores/`
- `/api/turmas/`
- `/api/alunos/`

### Autenticação para Testes

Acesse `http://localhost:8000/api/auth/login/` para fazer login via interface web do Django REST Framework.

## 🌐 Endpoints da API

### Professores

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| GET | `/api/professores/` | Lista todos os professores | Não |
| GET | `/api/professores/{id}/` | Detalhes de um professor | Não |
| POST | `/api/professores/` | Cria um novo professor | Sim |
| PUT | `/api/professores/{id}/` | Atualiza um professor | Sim |
| PATCH | `/api/professores/{id}/` | Atualiza parcialmente | Sim |
| DELETE | `/api/professores/{id}/` | Remove um professor | Sim |
| GET | `/api/professores/{id}/turmas/` | Lista turmas do professor | Não |

### Turmas

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| GET | `/api/turmas/` | Lista todas as turmas | Não |
| GET | `/api/turmas/{id}/` | Detalhes de uma turma | Não |
| POST | `/api/turmas/` | Cria uma nova turma | Sim |
| PUT | `/api/turmas/{id}/` | Atualiza uma turma | Sim |
| PATCH | `/api/turmas/{id}/` | Atualiza parcialmente | Sim |
| DELETE | `/api/turmas/{id}/` | Remove uma turma | Sim |
| GET | `/api/turmas/{id}/alunos/` | Lista alunos da turma | Sim |
| POST | `/api/turmas/{id}/matricular-aluno/` | Matricula um aluno | Sim |
| POST | `/api/turmas/{id}/desmatricular-aluno/` | Desmatricula um aluno | Sim |

### Alunos

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| GET | `/api/alunos/` | Lista todos os alunos | Não |
| GET | `/api/alunos/{id}/` | Detalhes de um aluno | Não |
| POST | `/api/alunos/` | Cria um novo aluno | Sim |
| PUT | `/api/alunos/{id}/` | Atualiza um aluno | Sim |
| PATCH | `/api/alunos/{id}/` | Atualiza parcialmente | Sim |
| DELETE | `/api/alunos/{id}/` | Remove um aluno | Sim |
| GET | `/api/alunos/{id}/turmas/` | Lista turmas do aluno | Sim |
| POST | `/api/alunos/{id}/matricular/` | Matricula em uma turma | Sim |
| POST | `/api/alunos/{id}/desmatricular/` | Desmatricula de uma turma | Sim |

## 📊 Modelos de Dados

### Professor

```python
{
    "id": Integer (auto),
    "nome": String(255),
    "email": Email (único),
    "departamento": String(100),
    "ativo": Boolean (padrão: true),
    "data_cadastro": DateTime (auto)
}
```

### Turma

```python
{
    "id": Integer (auto),
    "nome": String(255),
    "descricao": Text (opcional),
    "professor": ForeignKey(Professor) (opcional),
    "data_inicio": Date,
    "data_fim": Date,
    "status": Choice["Ativa", "Concluída", "Cancelada"]
}
```

### Aluno

```python
{
    "id": Integer (auto),
    "nome": String(255),
    "matricula": String(50) (único),
    "email": Email (único),
    "curso": String(100),
    "data_nascimento": Date,
    "genero": Choice["Masculino", "Feminino", "Outro", "Não Informado"],
    "turmas": ManyToMany(Turma)
}
```

## 🔐 Autenticação

O sistema suporta dois métodos de autenticação:

### 1. Session Authentication
Usado automaticamente ao fazer login via interface web do Django REST Framework.

### 2. Token Authentication

**Obter Token:**
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "sua_senha"}'
```

**Usar Token:**
```bash
curl http://localhost:8000/api/professores/ \
  -H "Authorization: Token seu_token_aqui"
```

## 📝 Exemplos de Requisições

### Criar um Professor

```bash
POST /api/professores/
Content-Type: application/json
Authorization: Token seu_token_aqui

{
    "nome": "Dr. João Silva",
    "email": "joao.silva@universidade.edu",
    "departamento": "Ciência da Computação",
    "ativo": true
}
```

**Resposta:**
```json
{
    "id": 1,
    "nome": "Dr. João Silva",
    "email": "joao.silva@universidade.edu",
    "departamento": "Ciência da Computação",
    "ativo": true,
    "data_cadastro": "2024-12-14T10:30:00Z"
}
```

### Criar uma Turma

```bash
POST /api/turmas/
Content-Type: application/json
Authorization: Token seu_token_aqui

{
    "nome": "Estruturas de Dados - 2025.1",
    "descricao": "Introdução a estruturas de dados fundamentais",
    "professor": 1,
    "data_inicio": "2025-02-01",
    "data_fim": "2025-06-30",
    "status": "Ativa"
}
```

### Criar um Aluno

```bash
POST /api/alunos/
Content-Type: application/json
Authorization: Token seu_token_aqui

{
    "nome": "Maria Santos",
    "matricula": "2025001",
    "email": "maria.santos@estudante.edu",
    "curso": "Engenharia de Software",
    "data_nascimento": "2003-05-15",
    "genero": "Feminino",
    "turmas": []
}
```

### Matricular Aluno em Turma

```bash
POST /api/alunos/1/matricular/
Content-Type: application/json
Authorization: Token seu_token_aqui

{
    "turma_id": 1
}
```

### Listar Alunos de uma Turma

```bash
GET /api/turmas/1/alunos/
Authorization: Token seu_token_aqui
```


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


## 📚 Recursos Adicionais

- [Documentação do Django](https://docs.djangoproject.com/)
- [Documentação do Django REST Framework](https://www.django-rest-framework.org/)
- [Tutorial Python](https://docs.python.org/3/tutorial/)


