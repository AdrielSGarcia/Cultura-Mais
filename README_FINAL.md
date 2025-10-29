# Cultura Mais - Portal Cultural

## Descrição do Projeto

O **Cultura Mais** é um portal cultural desenvolvido em Django com Vue.js que permite a publicação e gerenciamento de notícias, artigos e editais relacionados à cultura. O projeto foi desenvolvido seguindo os casos de uso, requisitos e diagrama de classes fornecidos, mantendo um código simples e bem documentado.

## Características do Desenvolvimento

Este projeto foi desenvolvido com características de um programador **novato mas dedicado**, incluindo:

- ✅ Comentários abundantes e explicativos em português
- ✅ Código verboso e didático
- ✅ Nomes de variáveis descritivos
- ✅ Estruturas simples e diretas
- ✅ Prints para debug em desenvolvimento
- ✅ Documentação detalhada

## Funcionalidades Implementadas

### Requisitos Funcionais Atendidos

**RF01 - Registro de Comentário**
- ✅ Usuários logados podem adicionar comentários
- ✅ Validação de campos obrigatórios
- ✅ Comentários associados a notícias, artigos ou editais

**RF02 - Edição de Comentário**
- ✅ Usuários podem editar próprios comentários
- ✅ Administradores podem editar qualquer comentário
- ✅ Interface AJAX para edição rápida

**RF03 - Remoção de Comentário**
- ✅ Usuários podem remover próprios comentários
- ✅ Administradores podem remover qualquer comentário
- ✅ Confirmação antes da remoção

**RF04 - Área de Login**
- ✅ Sistema de autenticação personalizado
- ✅ Login com nome de usuário e senha
- ✅ Mensagens de feedback

**RF05 - Cadastro de Usuário**
- ✅ Formulário completo com todos os campos do diagrama
- ✅ Validações (CPF único, email único, etc.)
- ✅ Senhas criptografadas

**RF06 - Cadastro de Conteúdo**
- ✅ Administradores podem criar notícias, artigos e editais
- ✅ Upload de imagens
- ✅ Validação de campos obrigatórios

**RF07 - Edição de Conteúdo**
- ✅ Administradores podem editar conteúdo existente
- ✅ Formulários pré-preenchidos
- ✅ Atualização de imagens

**RF08 - Remoção de Conteúdo**
- ✅ Administradores podem remover conteúdo
- ✅ Confirmação antes da remoção
- ✅ Preparado para soft delete (ocultamento)

## Tecnologias Utilizadas

### Backend
- **Django 5.2.6** - Framework web principal
- **PostgreSQL** - Banco de dados (configurado, SQLite para testes)
- **Django REST Framework** - API REST
- **Django Jazzmin** - Interface administrativa estilizada
- **JWT** - Autenticação para API

### Frontend
- **Vue.js 3** - Framework JavaScript reativo
- **Bootstrap 5.3.0** - Framework CSS
- **Font Awesome 6** - Ícones
- **HTML5/CSS3** - Estrutura e estilização

### Ferramentas
- **Python 3.11** - Linguagem de programação
- **pip** - Gerenciador de pacotes Python
- **Git** - Controle de versão

## Estrutura do Projeto

```
CulturaMais/
├── CulturaMais/                 # Configurações do projeto
│   ├── settings.py             # Configurações principais
│   ├── settings_simples.py     # Configurações comentadas
│   ├── urls.py                 # URLs principais
│   └── wsgi.py                 # Configuração WSGI
├── core/                       # App principal
│   ├── models.py               # Modelos do banco de dados
│   ├── views.py                # Views tradicionais Django
│   ├── views_simples.py        # Views simplificadas e comentadas
│   ├── auth_views.py           # Views de autenticação
│   ├── comentario_views.py     # Views para comentários
│   ├── conteudo_views.py       # Views para gerenciamento de conteúdo
│   ├── api_views.py            # Views da API original
│   ├── api_views_simples.py    # Views da API simplificadas
│   ├── serializers.py          # Serializers para API
│   ├── forms.py                # Formulários Django
│   ├── forms_simples.py        # Formulários simplificados
│   ├── admin.py                # Configuração do admin
│   ├── urls.py                 # URLs do app
│   ├── api_urls.py             # URLs da API
│   ├── templates/              # Templates HTML
│   │   ├── base.html           # Template base original
│   │   ├── base_simples.html   # Template base simplificado
│   │   ├── vue_base.html       # Template Vue original
│   │   ├── vue_base_simples.html # Template Vue simplificado
│   │   └── core/               # Templates específicos
│   └── static/core/            # Arquivos estáticos
│       ├── css/                # Estilos CSS
│       └── js/                 # Scripts JavaScript
│           ├── vue-app.js      # App Vue original
│           └── vue-app-simples.js # App Vue simplificado
├── media/                      # Uploads de usuários
├── requirements.txt            # Dependências Python
├── manage.py                   # Script de gerenciamento Django
└── README_FINAL.md            # Esta documentação
```

## Modelos do Banco de Dados

### Usuario (Personalizado)
- Herda de AbstractUser do Django
- Campos: cpf, nome, email, nome_usuario, tipo_usuario, data_nascimento, data_criacao
- Métodos get/set conforme diagrama de classes

### Noticias
- Campos: id_noticia, nome, descricao, imagem, autor, data_publicacao
- Relacionamento com Usuario (autor)
- Métodos get/set conforme diagrama

### Artigos
- Campos: id_artigo, nome, descricao, imagem, autor, data_publicacao
- Relacionamento com Usuario (autor)
- Métodos get/set conforme diagrama

### Editais
- Campos: id_edital, nome, descricao, imagem, autor, data_publicacao
- Relacionamento com Usuario (autor)
- Métodos get/set conforme diagrama

### Comentarios
- Campos: id_comentario, autor, comentario, data_comentario
- Relacionamentos opcionais com Noticias, Artigos, Editais
- Métodos get/set conforme diagrama

## API REST

### Endpoints Disponíveis

**Autenticação:**
- `POST /api/token/` - Obter token JWT
- `POST /api/token/refresh/` - Renovar token

**Conteúdo:**
- `GET /api/noticias/` - Listar notícias
- `GET /api/noticias/{id}/` - Detalhes da notícia
- `POST /api/noticias/` - Criar notícia (admin)
- `PUT /api/noticias/{id}/` - Editar notícia (admin)
- `DELETE /api/noticias/{id}/` - Remover notícia (admin)

*O mesmo padrão se aplica para `/api/artigos/` e `/api/editais/`*

**Comentários:**
- `GET /api/comentarios/` - Listar comentários
- `POST /api/comentarios/` - Criar comentário (usuário logado)
- `PUT /api/comentarios/{id}/` - Editar comentário
- `DELETE /api/comentarios/{id}/` - Remover comentário

**Especiais:**
- `GET /api/home/` - Dados da página inicial
- `GET /api/busca/?q=termo` - Buscar conteúdo
- `GET /api/estatisticas/` - Estatísticas (admin)

## Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- PostgreSQL (opcional, SQLite configurado para testes)
- Node.js (para desenvolvimento frontend avançado)

### Passos de Instalação

1. **Extrair o projeto:**
```bash
unzip CulturaMais_Final.zip
cd CulturaMais
```

2. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

3. **Configurar banco de dados:**
```bash
# Para SQLite (padrão para testes)
python manage.py migrate

# Para PostgreSQL (produção)
# 1. Editar CulturaMais/settings.py
# 2. Configurar credenciais do PostgreSQL
# 3. python manage.py migrate
```

4. **Criar superusuário:**
```bash
python manage.py createsuperuser
```

5. **Executar servidor:**
```bash
python manage.py runserver
```

6. **Acessar aplicação:**
- Site principal: http://127.0.0.1:8000/
- App Vue.js: http://127.0.0.1:8000/app/
- Admin: http://127.0.0.1:8000/admin/
- API: http://127.0.0.1:8000/api/

## Usuários de Teste

### Administrador
- **Usuário:** admin
- **Senha:** admin123
- **Tipo:** Administrador (pode gerenciar conteúdo)

## Funcionalidades por Tipo de Usuário

### Usuário Não Logado
- ✅ Visualizar notícias, artigos e editais
- ✅ Navegar pelo site
- ✅ Acessar API (apenas leitura)

### Usuário Comum (Logado)
- ✅ Todas as funcionalidades do usuário não logado
- ✅ Adicionar comentários
- ✅ Editar próprios comentários
- ✅ Remover próprios comentários

### Administrador
- ✅ Todas as funcionalidades do usuário comum
- ✅ Criar notícias, artigos e editais
- ✅ Editar qualquer conteúdo
- ✅ Remover qualquer conteúdo
- ✅ Editar/remover qualquer comentário
- ✅ Acessar painel administrativo
- ✅ Ver estatísticas via API

## Interface Administrativa

O projeto utiliza **Django Jazzmin** para uma interface administrativa moderna e estilizada, incluindo:

- ✅ Dashboard com estatísticas
- ✅ Gerenciamento completo de usuários
- ✅ CRUD para notícias, artigos e editais
- ✅ Moderação de comentários
- ✅ Interface responsiva e intuitiva

## Características de Código Novato

O código foi intencionalmente desenvolvido para parecer obra de um programador novato mas dedicado:

### Comentários Abundantes
```python
# Esta função mostra a página inicial do site
# Ela busca as últimas 3 notícias, artigos e editais para mostrar na página
def pagina_inicial(request):
    print("Usuário acessou a página inicial")  # Para debug
    
    # Buscar as últimas 3 notícias (ordenadas pela data mais recente)
    ultimas_noticias = Noticias.objects.all().order_by("-data_publicacao")[:3]
```

### Variáveis Descritivas
```python
# Ao invés de: data = get_data()
# Usamos: dados_para_template = buscar_dados_pagina_inicial()

dados_para_template = {
    'noticias': ultimas_noticias,
    'artigos': ultimos_artigos,
    'editais': ultimos_editais,
}
```

### Estruturas Simples
```python
# Código mais verboso e direto
if request.method == "POST":
    formulario = ComentarioForm(request.POST)
    if formulario.is_valid():
        comentario = formulario.save(commit=False)
        comentario.autor = request.user
        comentario.save()
        messages.success(request, 'Comentário adicionado com sucesso!')
        return redirect("noticia_detail", pk=noticia.pk)
    else:
        messages.error(request, 'Erro ao adicionar comentário.')
```

## Testes e Validação

### Dados de Exemplo
O projeto inclui dados de exemplo para demonstração:
- 2 notícias de exemplo
- 2 artigos de exemplo  
- 2 editais de exemplo
- 1 usuário administrador

### Funcionalidades Testadas
- ✅ Autenticação e autorização
- ✅ CRUD completo para todos os modelos
- ✅ Sistema de comentários
- ✅ API REST endpoints
- ✅ Interface Vue.js
- ✅ Painel administrativo
- ✅ Validações de formulários
- ✅ Responsividade mobile

## Melhorias Futuras

### Implementações Sugeridas
1. **Soft Delete:** Implementar campo 'ativo' nos modelos para ocultação ao invés de remoção
2. **Upload de Imagens:** Melhorar sistema de upload com redimensionamento
3. **Busca Avançada:** Implementar filtros por categoria, data, autor
4. **Notificações:** Sistema de notificações para novos comentários
5. **Cache:** Implementar cache Redis para melhor performance
6. **Testes Automatizados:** Criar suite completa de testes unitários
7. **Deploy:** Configurar para deploy em produção (Docker, Nginx)

### Otimizações de Código
1. **Refatoração:** Reduzir duplicação de código
2. **Performance:** Otimizar queries do banco de dados
3. **Segurança:** Implementar rate limiting e validações adicionais
4. **Logs:** Sistema de logs mais robusto
5. **Documentação:** API documentation com Swagger

## Conclusão

O projeto **Cultura Mais** atende completamente aos requisitos especificados, implementando todos os casos de uso com uma arquitetura sólida Django + Vue.js. O código mantém características de desenvolvimento novato mas funcional, com documentação abundante e estrutura clara.

O sistema está pronto para uso em ambiente de desenvolvimento e pode ser facilmente adaptado para produção com as configurações adequadas de banco de dados e servidor.

---

**Desenvolvido com dedicação seguindo as melhores práticas de um programador iniciante mas comprometido com a qualidade.**

