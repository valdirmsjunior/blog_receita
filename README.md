# 🥘 Receitaria - Blog de Receitas Profissional

O **Receitaria** é um sistema de gerenciamento de conteúdo (CMS) especializado em gastronomia, desenvolvido para dominar o ciclo completo de uma aplicação web. O projeto foca em escalabilidade, URLs amigáveis (SEO) e uma experiência de administração robusta.

## 🚀 Tecnologias Utilizadas

- **Python 3.14.0** (Ambiente gerenciado via `pyenv`)
- **Django 6.0** (Arquitetura MVT - Model-View-Template)
- **PostgreSQL** (Banco de dados relacional de alta performance)
- **Tailwind CSS** (Design responsivo e moderno)
- **Pillow** (Processamento de imagens de receitas e uploads)
- **Python-dotenv** (Gestão de variáveis de ambiente e segurança)

## 🌟 Funcionalidades Principais

- **Gestão Dinâmica:** Cadastro de receitas e categorias via painel do Django Admin.
- **Busca Inteligente:** Sistema de pesquisa iterativo que filtra por fragmentos de título ou ingredientes simulando buscas eficientes (usando objetos Q).
- **Arquitetura de Dados:** Relacionamento `ForeignKey` robusto entre Receitas e Categorias, atrelado à estratégia de referências fortes na proteção de integridade (`PROTECT`).
- **SEO Friendly:** Geração automática e dinâmica de `slugs` para assegurar URLs amigáveis para os motores de busca.
- **Media Handling:** Sistema completo de upload e exposição de mídias de imagem para a capa das receitas.
- **Integração de Templates:** Uso inteligente da tag de expansão de templates `Extends` usando páginas-base globais (como `base.html`) seguindo puramente os preceitos do DRY (Don't Repeat Yourself).

## 📂 Estrutura de Pastas

```text
blog_receitas/
├── blog/             # Configurações centrais do Django (settings, urls principais)
├── receita/          # App principal (Models, Views, URLs das receitas)
│   ├── templatetags/ # Filtros e Tags customizadas do Django Templates
│   └── templates/    # HTMLs específicos da Aplicação
├── static/           # Arquivos estáticos globais servidos ao front-end (CSS, JS)
├── media/            # Uploads transacionais de usuários em ambiente DEV (Imagens das receitas)
├── templates/        # Templates básicos e estruturais que abraçam o projeto (base.html)
├── requirements.txt  # Manifestos de dependências Python para congelar e clonar o projeto
└── .env              # Variáveis sigilosas vitais da máquina local (DB_*, SECRET_KEY)
```

## 🛠️ Instalação e Configuração (Desenvolvimento Local)

Estas instruções ajudarão você a colocar o projeto rodando na sua máquina visando testes e continuação do desenvolvimento (ambiente Apple Silicon M1, M2 ou compatíveis, e adaptável ao Linux).

### 1. Preparo Inicial do Repositório

Navegue ao ambiente que conterá o projeto (caso clonado via git) e ingresse à raiz diretiva:
```bash
git clone <url-do-repositorio> # Apenas se o código tiver de versão externa remota
cd blog_receitas
```

### 2. Configurando a Lógica Python

Acople e garanta a versão exata do Python, via Pyenv, antes de gerar as instalações para contornar discrepâncias em pacotes:
```bash
pyenv local 3.14.0
```

Forme e acione de forma hermética um ambiente virtual local:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Resolvendo Dependências

No mesmo Terminal logado ativado da virtualização, conclua a injeção dos pacotes requeridos contidos por `requirements.txt`:
```bash
pip install -r requirements.txt
```
> *(Se o `requirements.txt` não existir, use de modo verboso e individual: `pip install django psycopg2-binary Pillow python-dotenv`)*

### 4. Estabelecendo o Sigilo Local (Variáveis)

Não exponha chaves! Construa e proteja rigorosamente um arquivo `.env` na própria camada limiar da raiz dos diretórios e parametrize os fluxos:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=blog_receitas
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

### 5. Arquitetando o Banco de Dados

Suba e consolide as lógicas das models para a tabela do DB:
```bash
# Acione a criação explícita do Banco de Dados no Postgres da sua máquina primeiramente:
createdb blog_receitas

# Espelhe as regras do Schema de Dados a partir da modelagem do Django:
python manage.py makemigrations
python manage.py migrate
```

### 6. Executando o Projeto

Para a correta condução dos painéis de administrador, fundamente perfis de autoridade (Superusuário):
```bash
python manage.py createsuperuser
```

Gire a manivela para colocar a API de pé em conformidade com as lógicas atreladas:
```bash
python manage.py runserver
```

Feito! Abra no Browser de sua preferência:
- Ponto de Roteamento Principal (Blog Oficial): [http://localhost:8000/](http://localhost:8000/)
- Backoffice de Gerenciamento: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

📝 **Avisos Importantes:**
* Lembre-se, o serviço de PostgreSQL precisa necessariamente estar rodando como serviço (ou binário container) na sua base física em porta de resposta `:5432` antes da rodada do migration.  
* As imagens depositadas em ambientes de teste não persistem no projeto para reuso do versionamento. O arquivo `.gitignore` inativa explicitamente rastros de lixos para os `media/` de subpastas a evitar vazamentos gigantes no Github.
