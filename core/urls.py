from django.urls import path
from . import views
from .auth_views import cadastro_usuario_view, AutenticacaoLoginView, AutenticacaoLogoutView
from .vue_views import VueAppView
from .comentario_views import (
    adicionar_comentario, editar_comentario, remover_comentario,
    comentario_ajax_edit, comentario_ajax_delete, listar_comentarios_usuario
)
from .conteudo_views import (
    criar_noticia, criar_artigo, criar_edital,
    editar_noticia, editar_artigo, editar_edital,
    remover_noticia, remover_artigo, remover_edital,
    gerenciar_conteudo
)

urlpatterns = [
    # Vue.js App (main route)
    path("app/", VueAppView.as_view(), name="vue_app"),
    
    # Traditional Django views (for backward compatibility)
    path("", views.home, name="home"),
    path("noticias/", views.noticia_list, name="noticia_list"),
    path("noticias/<int:pk>/", views.noticia_detail, name="noticia_detail"),
    path("artigos/", views.artigo_list, name="artigo_list"),
    path("artigos/<int:pk>/", views.artigo_detail, name="artigo_detail"),
    path("editais/", views.edital_list, name="edital_list"),
    path("editais/<int:pk>/", views.edital_detail, name="edital_detail"),
    
    # Autenticação (RF04, RF05)
    path("register/", cadastro_usuario_view, name="register"),
    path("login/", AutenticacaoLoginView.as_view(), name="login"),
    path("logout/", AutenticacaoLogoutView.as_view(), name="logout"),
    
    # Gerenciamento de comentários (RF01, RF02, RF03)
    path("comentario/adicionar/", adicionar_comentario, name="adicionar_comentario"),
    path("comentario/<int:comentario_id>/editar/", editar_comentario, name="editar_comentario"),
    path("comentario/<int:comentario_id>/remover/", remover_comentario, name="remover_comentario"),
    path("comentario/<int:comentario_id>/ajax/edit/", comentario_ajax_edit, name="comentario_ajax_edit"),
    path("comentario/<int:comentario_id>/ajax/delete/", comentario_ajax_delete, name="comentario_ajax_delete"),
    path("usuario/<int:usuario_id>/comentarios/", listar_comentarios_usuario, name="listar_comentarios_usuario"),
    
    # Gerenciamento de conteúdo (RF06, RF07, RF08)
    path("admin/gerenciar/", gerenciar_conteudo, name="gerenciar_conteudo"),
    
    # Criação de conteúdo (RF06)
    path("admin/noticia/criar/", criar_noticia, name="criar_noticia"),
    path("admin/artigo/criar/", criar_artigo, name="criar_artigo"),
    path("admin/edital/criar/", criar_edital, name="criar_edital"),
    
    # Edição de conteúdo (RF07)
    path("admin/noticia/<int:pk>/editar/", editar_noticia, name="editar_noticia"),
    path("admin/artigo/<int:pk>/editar/", editar_artigo, name="editar_artigo"),
    path("admin/edital/<int:pk>/editar/", editar_edital, name="editar_edital"),
    
    # Remoção de conteúdo (RF08)
    path("admin/noticia/<int:pk>/remover/", remover_noticia, name="remover_noticia"),
    path("admin/artigo/<int:pk>/remover/", remover_artigo, name="remover_artigo"),
    path("admin/edital/<int:pk>/remover/", remover_edital, name="remover_edital"),
    
    # URLs antigas para compatibilidade
    path("noticias/<int:pk>/comment/", views.add_comment_to_noticia, name="add_comment_to_noticia"),
    path("artigos/<int:pk>/comment/", views.add_comment_to_artigo, name="add_comment_to_artigo"),
    path("editais/<int:pk>/comment/", views.add_comment_to_edital, name="add_comment_to_edital"),
]

