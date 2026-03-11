🥘 Receitaria - Blog de Receitas Profissional
O Receitaria é um sistema de gerenciamento de conteúdo (CMS) especializado em gastronomia, desenvolvido para dominar o ciclo completo de uma aplicação Django 6.0. O projeto foca em escalabilidade, URLs amigáveis (SEO) e uma experiência de administração robusta.

🚀 Tecnologias Utilizadas
Python 3.14.0 (Ambiente gerenciado via pyenv)

Django 6.0 (MVT Architecture)

PostgreSQL (Banco de dados relacional de alta performance)

Tailwind CSS (Design responsivo e moderno)

Pillow (Processamento de imagens de receitas)

Python-dotenv (Gestão de variáveis de ambiente e segurança)

🌟 Funcionalidades Principais
Gestão Dinâmica: Cadastro de receitas e categorias via Django Admin.

Busca Inteligente: Sistema de pesquisa que filtra por título e ingredientes usando objetos Q (Busca Complexa).

Arquitetura de Dados: Relacionamento ForeignKey entre Receitas e Categorias com proteção de integridade (PROTECT).

SEO Friendly: Geração automática de slugs para URLs amigáveis e otimizadas para motores de busca.

Media Handling: Sistema de upload e servimento de imagens configurado para ambiente de desenvolvimento.

Template Inheritance: Uso avançado de base.html para evitar repetição de código (DRY).

📂 Estrutura de Pastas
blog_receitas/
├── blog/ # Configurações centrais do projeto
├── receita/ # App principal (Models, Views, URLs)
│ ├── templatetags/ # Filtros e Tags customizadas
│ └── templates/ # HTMLs específicos da App
├── static/ # Arquivos globais (CSS, JS, Imagens do sistema)
├── media/ # Uploads dos usuários (Fotos das receitas)
├── templates/ # Base global (base.html)
└── .env # Variáveis sensíveis (DB, Secret Key)

🛠️ Instalação e Configuração (MacBook M1)
Clone o projeto e entre na pasta:
cd blog_receitas

Configure a versão do Python:
pyenv local 3.14.0

Crie e ative o ambiente virtual:
python3 -m venv .venv
source .venv/bin/activate

Instale as dependências:
pip install django psycopg2-binary Pillow python-dotenv

Configure o arquivo .env na raiz:
DB_ENGINE=django.db.backends.postgresql
DB_NAME=blog_receitas
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

Crie o banco de dados no Postgres e rode as migrações:
createdb blog_receitas
python manage.py makemigrations
python manage.py migrate

Inicie o servidor:
python manage.py runserver
