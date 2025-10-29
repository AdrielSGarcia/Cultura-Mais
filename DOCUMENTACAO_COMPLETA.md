# Documentação Completa do Sistema Cultura Mais

## 1. Visão Geral do Projeto

O sistema **Cultura Mais** é um portal cultural dinâmico desenvolvido para gerenciar e exibir notícias, artigos e editais relacionados à cultura. Ele foi construído utilizando o framework web Django para o backend e o framework JavaScript Vue.js para o frontend, proporcionando uma experiência de usuário moderna e responsiva. O projeto segue uma arquitetura RESTful para a comunicação entre frontend e backend.

O desenvolvimento foi guiado por um conjunto de casos de uso, requisitos e um diagrama de classes detalhado, garantindo que todas as funcionalidades essenciais fossem implementadas de forma estruturada. Uma característica notável deste projeto é a intencionalidade de manter o código com um estilo que remete a um **desenvolvedor novato, porém dedicado**, com foco em clareza, verbosidade e comentários explicativos abundantes.

## 2. Requisitos e Casos de Uso Atendidos

Todos os requisitos funcionais (RF) e casos de uso especificados na documentação original foram implementados:

### 2.1. Sistema de Comentários (RF01, RF02, RF03)

-   **RF01 - Registro de Comentário:** Usuários autenticados podem adicionar comentários a notícias, artigos e editais. O sistema valida se o campo de comentário não está vazio antes de salvar.
-   **RF02 - Edição de Comentário:** Usuários podem editar seus próprios comentários. Administradores têm permissão para editar qualquer comentário. A edição é facilitada por uma interface AJAX para uma experiência mais fluida.
-   **RF03 - Remoção de Comentário:** Usuários podem remover seus próprios comentários, e administradores podem remover qualquer comentário. A remoção é realizada com uma confirmação prévia e, embora atualmente implementada como exclusão física, o código está preparado para um 


abordagem de *soft delete* (ocultamento lógico) no futuro.

### 2.2. Sistema de Autenticação (RF04, RF05)

-   **RF04 - Área de Login:** Implementa um sistema de login personalizado que permite aos usuários autenticar-se usando seu nome de usuário e senha. Inclui mensagens de feedback para sucesso ou falha no login.
-   **RF05 - Cadastro de Usuário:** Oferece um formulário de cadastro completo, alinhado com o diagrama de classes, que coleta informações como nome completo, CPF, e-mail, nome de usuário e data de nascimento. O sistema realiza validações para garantir a unicidade do CPF e e-mail, além de verificar a conformidade das senhas.

### 2.3. Gerenciamento de Conteúdo (RF06, RF07, RF08)

-   **RF06 - Cadastro de Conteúdo:** Administradores podem criar e publicar novos itens de conteúdo, incluindo notícias, artigos e editais. O sistema suporta o upload de imagens e valida a presença de campos obrigatórios.
-   **RF07 - Edição de Conteúdo:** Administradores podem modificar qualquer notícia, artigo ou edital existente. Os formulários de edição são pré-preenchidos com os dados atuais e permitem a atualização de imagens.
-   **RF08 - Remoção de Conteúdo:** Administradores têm a capacidade de remover notícias, artigos e editais. Uma confirmação é solicitada antes da exclusão, e a estrutura do código prevê uma futura implementação de *soft delete*.

## 3. Tecnologias Utilizadas

O projeto Cultura Mais é construído sobre uma pilha de tecnologias robusta e moderna:

### 3.1. Backend

-   **Django 5.2.6:** Framework web Python de alto nível que acelera o desenvolvimento de sites seguros e escaláveis. Utilizado para a lógica de negócios, gerenciamento de banco de dados (ORM) e API REST.
-   **PostgreSQL:** Sistema de gerenciamento de banco de dados relacional de código aberto, conhecido por sua robustez, confiabilidade e desempenho. É o banco de dados recomendado para produção, embora o projeto possa ser configurado para SQLite para desenvolvimento local rápido.
-   **Django REST Framework (DRF):** Um poderoso e flexível kit de ferramentas para construir APIs web. Facilita a criação de endpoints RESTful para que o frontend Vue.js possa interagir com os dados do backend.
-   **Django Jazzmin:** Uma interface administrativa personalizável e estilizada para o Django. Substitui o painel de administração padrão do Django por uma versão mais moderna e visualmente atraente, melhorando a experiência do administrador.
-   **JSON Web Tokens (JWT):** Utilizado para autenticação segura na API. Permite que os usuários façam login e recebam um token que pode ser usado para acessar recursos protegidos da API sem a necessidade de enviar credenciais a cada requisição.

### 3.2. Frontend

-   **Vue.js 3:** Um framework JavaScript progressivo para a construção de interfaces de usuário. Permite a criação de Single Page Applications (SPAs) reativas e eficientes, proporcionando uma experiência de usuário fluida.
-   **Bootstrap 5.3.0:** O framework de código aberto mais popular para desenvolver projetos responsivos e mobile-first na web. Fornece componentes CSS e JavaScript pré-construídos para estilização e layout.
-   **Font Awesome 6:** Uma biblioteca de ícones vetoriais escaláveis que podem ser facilmente personalizados com CSS. Utilizado para adicionar ícones visuais em todo o site, melhorando a usabilidade e a estética.
-   **HTML5/CSS3:** As linguagens fundamentais para a estrutura e estilização de páginas web, respectivamente.

### 3.3. Ferramentas de Desenvolvimento

-   **Python 3.11+:** A linguagem de programação principal utilizada no backend.
-   **pip:** O gerenciador de pacotes padrão para Python, usado para instalar e gerenciar as bibliotecas e dependências do projeto.
-   **Git:** Sistema de controle de versão distribuído, essencial para o gerenciamento colaborativo do código-fonte e rastreamento de alterações.

## 4. Estrutura do Projeto

A estrutura de diretórios do projeto é organizada para separar as configurações globais do Django (`CulturaMais/`) das funcionalidades específicas da aplicação (`core/`), além de incluir diretórios para arquivos estáticos, mídia e documentação:

```
CulturaMais/
├── CulturaMais/                 # Diretório principal do projeto Django
│   ├── settings.py             # Configurações principais do Django
│   ├── settings_simples.py     # Versão simplificada e comentada das configurações
│   ├── urls.py                 # Definições de URL globais do projeto
│   └── wsgi.py                 # Configuração WSGI para deploy
├── core/                       # Aplicação principal do Django (o "app" do site)
│   ├── models.py               # Definições dos modelos de dados (tabelas do banco)
│   ├── views.py                # Funções e classes que processam requisições HTTP (views tradicionais)
│   ├── views_simples.py        # Versão simplificada e comentada das views tradicionais
│   ├── auth_views.py           # Views específicas para autenticação de usuários
│   ├── comentario_views.py     # Views para gerenciamento de comentários
│   ├── conteudo_views.py       # Views para gerenciamento de notícias, artigos e editais
│   ├── api_views.py            # Views da API REST (versão original)
│   ├── api_views_simples.py    # Versão simplificada e comentada das views da API
│   ├── serializers.py          # Serializers para converter dados do modelo para JSON (e vice-versa)
│   ├── forms.py                # Definições de formulários Django
│   ├── forms_simples.py        # Versão simplificada e comentada dos formulários
│   ├── admin.py                # Configurações para o painel administrativo do Django
│   ├── urls.py                 # Definições de URL específicas do app `core`
│   ├── api_urls.py             # Definições de URL para a API REST
│   ├── templates/              # Diretório para arquivos de template HTML
│   │   ├── base.html           # Template base principal
│   │   ├── base_simples.html   # Template base simplificado e comentado
│   │   ├── vue_base.html       # Template base para a aplicação Vue.js
│   │   ├── vue_base_simples.html # Template base Vue.js simplificado e comentado
│   │   └── core/               # Subdiretório para templates específicos do app `core`
│   └── static/core/            # Diretório para arquivos estáticos (CSS, JS, imagens)
│       ├── css/                # Arquivos CSS
│       └── js/                 # Arquivos JavaScript
│           ├── vue-app.js      # Código JavaScript da aplicação Vue.js (original)
│           └── vue-app-simples.js # Código JavaScript da aplicação Vue.js (simplificado e comentado)
├── media/                      # Diretório para arquivos de mídia (uploads de usuários)
├── requirements.txt            # Lista de dependências Python do projeto
├── manage.py                   # Utilitário de linha de comando do Django
└── README_FINAL.md            # Documentação final do projeto
```

## 5. Modelos do Banco de Dados (core/models.py)

Os modelos foram cuidadosamente reestruturados para refletir o diagrama de classes, com cada modelo representando uma tabela no banco de dados. A seguir, uma descrição detalhada de cada um:

### 5.1. `Usuario` (Herda de `AbstractUser`)

Este modelo estende o modelo de usuário padrão do Django para incluir campos adicionais necessários para o sistema Cultura Mais. Ele representa tanto usuários comuns quanto administradores.

-   **`cpf`**: `CharField` (max_length=11, unique=True) - CPF do usuário, único e obrigatório.
-   **`nome`**: `CharField` (max_length=200) - Nome completo do usuário.
-   **`email`**: `EmailField` (unique=True) - Endereço de e-mail do usuário, único e obrigatório.
-   **`nome_usuario`**: `CharField` (max_length=150, unique=True) - Nome de usuário para login, único e obrigatório. Este campo é mapeado para o `username` padrão do Django.
-   **`password`**: (Herdado de `AbstractUser`) - Senha do usuário, armazenada de forma segura (hash).
-   **`tipo_usuario`**: `IntegerField` (default=0) - Define o tipo de usuário (0 para comum, 1 para administrador).
-   **`data_nascimento`**: `DateField` - Data de nascimento do usuário.
-   **`data_criacao`**: `DateTimeField` (auto_now_add=True) - Data e hora de criação da conta, preenchida automaticamente.

**Métodos (exemplo):**
-   `get_cpf()`, `set_cpf(cpf)`
-   `get_nome()`, `set_nome(nome)`
-   `get_email()`, `set_email(email)`
-   `get_nome_usuario()`, `set_nome_usuario(nome_usuario)`
-   `get_data_nascimento()`, `set_data_nascimento(data_nascimento)`
-   `get_tipo_usuario()`, `set_tipo_usuario(tipo_usuario)`
-   `get_data_criacao()`

### 5.2. `Noticias`

Representa as notícias publicadas no portal.

-   **`id_noticia`**: `AutoField` (primary_key=True) - Chave primária auto-incrementável.
-   **`nome`**: `CharField` (max_length=200) - Título da notícia.
-   **`descricao`**: `TextField` - Conteúdo completo da notícia.
-   **`imagem`**: `ImageField` (upload_to='noticias/', blank=True, null=True) - Imagem de destaque da notícia.
-   **`autor`**: `ForeignKey` para `Usuario` - O usuário que publicou a notícia.
-   **`data_publicacao`**: `DateTimeField` (auto_now_add=True) - Data e hora da publicação.

**Métodos (exemplo):**
-   `get_id()`, `set_id(id)`
-   `get_nome()`, `set_nome(nome)`
-   `get_descricao()`, `set_descricao(descricao)`
-   `get_imagem()`, `set_imagem(imagem)`
-   `get_autor()`, `set_autor(autor)`
-   `get_data_publicacao()`

### 5.3. `Artigos`

Representa os artigos publicados no portal.

-   **`id_artigo`**: `AutoField` (primary_key=True) - Chave primária auto-incrementável.
-   **`nome`**: `CharField` (max_length=200) - Título do artigo.
-   **`descricao`**: `TextField` - Conteúdo completo do artigo.
-   **`imagem`**: `ImageField` (upload_to='artigos/', blank=True, null=True) - Imagem de destaque do artigo.
-   **`autor`**: `ForeignKey` para `Usuario` - O usuário que publicou o artigo.
-   **`data_publicacao`**: `DateTimeField` (auto_now_add=True) - Data e hora da publicação.

**Métodos (exemplo):**
-   `get_id()`, `set_id(id)`
-   `get_nome()`, `set_nome(nome)`
-   `get_descricao()`, `set_descricao(descricao)`
-   `get_imagem()`, `set_imagem(imagem)`
-   `get_autor()`, `set_autor(autor)`
-   `get_data_publicacao()`

### 5.4. `Editais`

Representa os editais publicados no portal.

-   **`id_edital`**: `AutoField` (primary_key=True) - Chave primária auto-incrementável.
-   **`nome`**: `CharField` (max_length=200) - Título do edital.
-   **`descricao`**: `TextField` - Conteúdo completo do edital.
-   **`imagem`**: `ImageField` (upload_to='editais/', blank=True, null=True) - Imagem de destaque do edital.
-   **`autor`**: `ForeignKey` para `Usuario` - O usuário que publicou o edital.
-   **`data_publicacao`**: `DateTimeField` (auto_now_add=True) - Data e hora da publicação.

**Métodos (exemplo):**
-   `get_id()`, `set_id(id)`
-   `get_nome()`, `set_nome(nome)`
-   `get_descricao()`, `set_descricao(descricao)`
-   `get_imagem()`, `set_imagem(imagem)`
-   `get_autor()`, `set_autor(autor)`
-   `get_data_publicacao()`

### 5.5. `Comentarios`

Representa os comentários feitos pelos usuários em notícias, artigos ou editais.

-   **`id_comentario`**: `AutoField` (primary_key=True) - Chave primária auto-incrementável.
-   **`autor`**: `ForeignKey` para `Usuario` - O usuário que fez o comentário.
-   **`comentario`**: `TextField` - O texto do comentário.
-   **`data_comentario`**: `DateTimeField` (auto_now_add=True) - Data e hora do comentário.
-   **`noticia`**: `ForeignKey` para `Noticias` (null=True, blank=True) - Notícia à qual o comentário está associado (opcional).
-   **`artigo`**: `ForeignKey` para `Artigos` (null=True, blank=True) - Artigo ao qual o comentário está associado (opcional).
-   **`edital`**: `ForeignKey` para `Editais` (null=True, blank=True) - Edital ao qual o comentário está associado (opcional).

**Métodos (exemplo):**
-   `get_id()`, `set_id(id)`
-   `get_autor()`, `set_autor(autor)`
-   `get_comentario()`, `set_comentario(comentario)`
-   `get_data_comentario()`

## 6. API REST (core/api_views_simples.py e core/api_urls.py)

A API RESTful permite que o frontend Vue.js e outras aplicações interajam com os dados do backend. Ela foi construída usando Django REST Framework e inclui autenticação JWT.

### 6.1. Endpoints de Autenticação

-   **`POST /api/token/`**: Endpoint para login. O usuário envia `username` (nome de usuário) e `password` (senha) e recebe um par de tokens JWT (`access` e `refresh`).
-   **`POST /api/token/refresh/`**: Endpoint para renovar o token de acesso. O usuário envia o `refresh` token e recebe um novo `access` token.

### 6.2. Endpoints de Conteúdo (Notícias, Artigos, Editais)

Cada tipo de conteúdo (Notícias, Artigos, Editais) possui um conjunto completo de endpoints CRUD (Create, Retrieve, Update, Delete) gerados automaticamente pelo `DefaultRouter` do Django REST Framework.

-   **`GET /api/{tipo_conteudo}/`**: Lista todos os itens de um tipo de conteúdo (ex: `/api/noticias/`).
-   **`GET /api/{tipo_conteudo}/{id}/`**: Retorna os detalhes de um item específico (ex: `/api/noticias/1/`).
-   **`POST /api/{tipo_conteudo}/`**: Cria um novo item de conteúdo. Requer autenticação e permissões de administrador.
-   **`PUT /api/{tipo_conteudo}/{id}/`**: Atualiza um item de conteúdo existente. Requer autenticação e permissões de administrador.
-   **`DELETE /api/{tipo_conteudo}/{id}/`**: Remove um item de conteúdo. Requer autenticação e permissões de administrador.
-   **`GET /api/{tipo_conteudo}/{id}/comentarios/`**: Endpoint aninhado para listar os comentários de um item de conteúdo específico (ex: `/api/noticias/1/comentarios/`).

### 6.3. Endpoints de Comentários

-   **`GET /api/comentarios/`**: Lista todos os comentários.
-   **`POST /api/comentarios/`**: Cria um novo comentário. Requer autenticação. O comentário é associado ao usuário logado e ao item de conteúdo (notícia, artigo ou edital) via IDs fornecidos no corpo da requisição.
-   **`PUT /api/comentarios/{id}/`**: Atualiza um comentário existente. Requer autenticação e permissão (autor do comentário ou administrador).
-   **`DELETE /api/comentarios/{id}/`**: Remove um comentário existente. Requer autenticação e permissão (autor do comentário ou administrador).

### 6.4. Endpoints Especiais

-   **`GET /api/home/`**: Retorna os dados necessários para a página inicial do site, incluindo as últimas notícias, artigos e editais. Não requer autenticação.
-   **`GET /api/busca/?q=termo`**: Realiza uma busca geral por um termo em notícias, artigos e editais. Não requer autenticação.
-   **`GET /api/estatisticas/`**: Retorna estatísticas gerais do site (número total de notícias, artigos, editais, comentários, usuários). Requer autenticação e permissões de administrador.

## 7. Frontend Vue.js (core/static/core/js/vue-app-simples.js e core/templates/vue_base_simples.html)

O frontend é uma Single Page Application (SPA) construída com Vue.js, que interage com a API REST do Django para exibir e gerenciar o conteúdo. O código Vue.js foi simplificado e extensivamente comentado para facilitar o entendimento.

### 7.1. Estrutura da Aplicação Vue.js

-   **`aplicacaoCulturaMais` (instância Vue):** Objeto principal da aplicação Vue, montado no elemento `<div id="app">`.
-   **`data()`:** Contém o estado reativo da aplicação, como `carregando` (status de carregamento), `paginaAtual` (página exibida), `usuario` (dados do usuário logado), `dadosHome` (dados da página inicial), `noticias`, `artigos`, `editais`, `alerta` (para mensagens ao usuário), `textoBusca` e `resultadosBusca`.
-   **`methods`:** Contém as funções que manipulam o estado e interagem com a API:
    -   `mostrarAlerta(tipo, mensagem)`: Exibe mensagens de feedback ao usuário.
    -   `fazerRequisicao(url, opcoes)`: Função utilitária para realizar requisições HTTP para a API, incluindo tratamento de erros e envio do token CSRF.
    -   `obterTokenCSRF()`: Extrai o token CSRF dos cookies para segurança nas requisições POST.
    -   `carregarDadosHome()`, `carregarNoticias()`, `carregarArtigos()`, `carregarEditais()`: Funções assíncronas para buscar dados da API.
    -   `navegarPara(pagina, id)`: Altera a página atual da SPA e carrega os dados correspondentes.
    -   `adicionarComentario(tipo, id)`, `iniciarEdicaoComentario(comentarioId, textoAtual)`, `cancelarEdicaoComentario()`, `salvarEdicaoComentario(comentarioId)`, `removerComentario(comentarioId)`: Funções para gerenciar comentários, interagindo com os endpoints de comentários da API.
    -   `alternarMenuMobile()`: Controla a visibilidade do menu de navegação em dispositivos móveis.
    -   `formatarData(dataString)`: Função utilitária para formatar datas.
-   **`mounted()`:** Hook do ciclo de vida do Vue que é executado quando a aplicação é criada. Utilizado para carregar os dados iniciais da página home.

### 7.2. Template Vue.js (`vue_base_simples.html`)

Este template define a estrutura HTML da aplicação Vue.js, incluindo a barra de navegação, área de alertas, conteúdo principal e rodapé. Ele utiliza diretivas Vue (`v-if`, `v-for`, `@click`, `:class`) para renderizar dinamicamente o conteúdo com base no estado da aplicação.

-   **Barra de Navegação:** Inclui links para as diferentes seções do site (Início, Notícias, Artigos, Editais) e opções de autenticação (Entrar, Cadastrar, Perfil do Usuário, Sair).
-   **Área de Alertas:** Exibe mensagens de sucesso, erro ou informação para o usuário.
-   **Conteúdo Principal:** A seção central onde o conteúdo das páginas (home, lista de notícias, detalhes de notícias, etc.) é renderizado condicionalmente.
-   **Rodapé:** Contém informações de copyright e links úteis.

## 8. Interface Administrativa (core/admin.py e Django Jazzmin)

O painel administrativo foi aprimorado com o Django Jazzmin para oferecer uma experiência de gerenciamento mais agradável e funcional. As configurações no `core/admin.py` definem como cada modelo é exibido e gerenciado no painel.

-   **`UsuarioAdmin`:** Configuração personalizada para o modelo `Usuario`, incluindo campos visíveis na lista, filtros, campos de busca e *fieldsets* para organização dos campos no formulário de edição/criação.
-   **`NoticiasAdmin`, `ArtigosAdmin`, `EditaisAdmin`:** Configurações semelhantes para os modelos de conteúdo, definindo `list_display`, `list_filter`, `search_fields` e `fieldsets`.
-   **`ComentariosAdmin`:** Configuração para o modelo `Comentarios`, com métodos personalizados (`get_comentario_resumo`, `get_conteudo_relacionado`) para exibir informações relevantes na lista de comentários.
-   **Personalização Jazzmin:** O `settings.py` contém configurações para o Jazzmin, como título do site, cabeçalho, links do menu superior e ícones personalizados para cada modelo, garantindo uma interface visualmente atraente e fácil de usar.

## 9. Características de Código Novato

Para atender ao requisito de parecer um projeto de um desenvolvedor novato mas dedicado, diversas práticas foram adotadas:

-   **Comentários Abundantes:** Cada arquivo Python e HTML, bem como as funções e blocos de código importantes, contêm comentários detalhados em português, explicando o propósito e o funcionamento do código. Isso torna o código extremamente legível e didático.
-   **Verbosiade e Clareza:** Preferência por código mais verboso e explícito em detrimento de soluções excessivamente concisas ou 


abstratas. Variáveis e funções têm nomes descritivos (muitas vezes em português) que indicam claramente seu propósito.
-   **Uso de `print()` para Debug:** O código inclui várias chamadas `print()` para depuração, uma prática comum entre desenvolvedores iniciantes para rastrear o fluxo de execução e o estado das variáveis.
-   **Estruturas Simples:** Evita-se o uso de padrões de design complexos ou otimizações prematuras. A lógica é implementada de forma direta, passo a passo, facilitando o acompanhamento.
-   **Documentação Detalhada:** Além dos comentários no código, esta documentação abrangente serve como um guia completo para entender cada aspecto do sistema.

## 10. Instalação e Configuração

Para configurar e executar o projeto Cultura Mais, siga os passos abaixo:

### 10.1. Pré-requisitos

-   **Python 3.11+:** Certifique-se de ter o Python instalado em seu sistema.
-   **PostgreSQL:** O banco de dados principal para o projeto. Certifique-se de ter um servidor PostgreSQL em execução e as credenciais de acesso (nome do banco de dados, usuário, senha, host, porta).
-   **pip:** Gerenciador de pacotes Python (geralmente vem com o Python).

### 10.2. Passos de Instalação

1.  **Extrair o Projeto:**
    Descompacte o arquivo `CulturaMais_Final_Completo.zip` em um diretório de sua escolha.
    ```bash
    unzip CulturaMais_Final_Completo.zip
    cd CulturaMais
    ```

2.  **Instalar Dependências Python:**
    Instale todas as bibliotecas Python necessárias listadas no arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurar Banco de Dados (PostgreSQL):**
    Edite o arquivo `CulturaMais/settings.py` e configure as credenciais do seu banco de dados PostgreSQL. Certifique-se de que o banco de dados `culturamais_db` (ou o nome que você escolher) exista e que o usuário `culturamais_user` (ou o seu usuário) tenha permissões para acessá-lo.

    ```python
    # CulturaMais/settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'culturamais_db',         # Nome do seu banco de dados
            'USER': 'culturamais_user',       # Seu usuário do PostgreSQL
            'PASSWORD': 'culturamais_password', # Sua senha do PostgreSQL
            'HOST': 'localhost',              # Endereço do seu servidor PostgreSQL
            'PORT': '',                       # Porta do PostgreSQL (geralmente 5432)
        }
    }
    ```

4.  **Aplicar Migrações:**
    Execute as migrações do Django para criar as tabelas no banco de dados.
    ```bash
    python manage.py migrate
    ```

5.  **Criar Superusuário:**
    Crie um superusuário para acessar o painel administrativo. Você será solicitado a fornecer um nome de usuário, e-mail e senha.
    ```bash
    python manage.py createsuperuser
    ```
    *Nota: Um superusuário `admin` com senha `admin123` já foi criado para testes, mas você pode criar outro se desejar.*

6.  **Coletar Arquivos Estáticos:**
    Para o deploy, é importante coletar todos os arquivos estáticos em um único diretório.
    ```bash
    python manage.py collectstatic
    ```

7.  **Executar o Servidor de Desenvolvimento:**
    Inicie o servidor de desenvolvimento do Django.
    ```bash
    python manage.py runserver
    ```

8.  **Acessar a Aplicação:**
    -   **Site Principal:** `http://127.0.0.1:8000/`
    -   **App Vue.js:** `http://127.0.0.1:8000/app/`
    -   **Painel Administrativo:** `http://127.0.0.1:8000/admin/`
    -   **API REST:** `http://127.0.0.1:8000/api/`

## 11. Usuários de Teste

Para facilitar os testes, um usuário administrador foi criado:

-   **Usuário:** `admin`
-   **Senha:** `admin123`
-   **Tipo:** Administrador (com acesso total ao gerenciamento de conteúdo e painel administrativo).

## 12. Funcionalidades por Tipo de Usuário

### 12.1. Usuário Não Logado

-   Visualizar notícias, artigos e editais.
-   Navegar por todas as páginas públicas do site.
-   Acessar endpoints da API que não requerem autenticação (apenas leitura).

### 12.2. Usuário Comum (Logado)

-   Todas as funcionalidades do usuário não logado.
-   Adicionar comentários a qualquer item de conteúdo.
-   Editar seus próprios comentários.
-   Remover seus próprios comentários.

### 12.3. Administrador

-   Todas as funcionalidades do usuário comum.
-   Criar, editar e remover notícias, artigos e editais.
-   Editar e remover qualquer comentário.
-   Acessar o painel administrativo (Django Jazzmin).
-   Visualizar estatísticas gerais do site via API.

## 13. Melhorias Futuras e Otimizações

Embora o projeto esteja completo e funcional, algumas melhorias e otimizações podem ser consideradas para um desenvolvimento futuro:

### 13.1. Implementações Sugeridas

1.  **Soft Delete:** Implementar um campo `ativo` (ou similar) nos modelos de conteúdo e comentários para que, ao invés de remover itens do banco de dados, eles sejam apenas marcados como inativos. Isso permite a recuperação de dados e mantém um histórico.
2.  **Upload de Imagens Avançado:** Melhorar o sistema de upload de imagens com funcionalidades como redimensionamento automático, otimização para web e integração com serviços de armazenamento em nuvem (ex: AWS S3).
3.  **Busca Avançada:** Expandir a funcionalidade de busca para incluir filtros por categoria, data de publicação, autor e outros critérios, além da busca por texto livre.
4.  **Sistema de Notificações:** Implementar um sistema de notificações para alertar usuários sobre novos comentários em seus posts ou outras interações relevantes.
5.  **Cache:** Integrar um sistema de cache (como Redis) para melhorar a performance do site, especialmente em páginas com alto tráfego ou dados que não mudam frequentemente.
6.  **Testes Automatizados:** Desenvolver uma suíte completa de testes unitários e de integração para garantir a estabilidade e a robustez do código a longo prazo.
7.  **Deploy em Produção:** Configurar o projeto para um ambiente de produção, incluindo Dockerização, uso de Nginx/Gunicorn, gerenciamento de variáveis de ambiente e monitoramento.

### 13.2. Otimizações de Código

1.  **Refatoração:** Revisar o código para reduzir a duplicação, aplicar princípios DRY (Don't Repeat Yourself) e melhorar a modularidade.
2.  **Performance de Queries:** Otimizar as consultas ao banco de dados para garantir que sejam eficientes, especialmente em cenários de alta carga.
3.  **Segurança:** Implementar medidas de segurança adicionais, como *rate limiting* para endpoints da API, validações mais robustas de entrada de dados e proteção contra ataques comuns (XSS, CSRF).
4.  **Logs:** Configurar um sistema de logging mais robusto para monitorar a aplicação em produção e facilitar a depuração de problemas.
5.  **Documentação da API:** Gerar documentação interativa da API (ex: com Swagger/OpenAPI) para facilitar o consumo por outros desenvolvedores.

## 14. Conclusão

O projeto **Cultura Mais** é uma plataforma cultural completa e funcional, desenvolvida com atenção aos detalhes e seguindo as especificações fornecidas. Ele demonstra uma abordagem de desenvolvimento clara e didática, ideal para quem busca entender a construção de aplicações web modernas com Django e Vue.js. O sistema está pronto para ser explorado, testado e expandido, servindo como uma base sólida para futuras iterações.

---

**Desenvolvido com dedicação e clareza, refletindo o trabalho de um programador iniciante comprometido com a qualidade e o aprendizado.**

