from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Noticias, Artigos, Editais, Comentarios

class UsuarioAdmin(UserAdmin):
    list_display = ('nome_usuario', 'nome', 'email', 'cpf', 'tipo_usuario', 'data_criacao', 'is_active')
    list_filter = ('tipo_usuario', 'is_active', 'data_criacao')
    search_fields = ('nome_usuario', 'nome', 'email', 'cpf')
    ordering = ('nome_usuario',)
    
    fieldsets = (
        ('Informações de Login', {
            'fields': ('nome_usuario', 'password')
        }),
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'cpf', 'data_nascimento')
        }),
        ('Permissões', {
            'fields': ('tipo_usuario', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Datas Importantes', {
            'fields': ('last_login', 'data_criacao')
        }),
    )
    
    add_fieldsets = (
        ('Criar Novo Usuário', {
            'classes': ('wide',),
            'fields': ('nome_usuario', 'nome', 'email', 'cpf', 'data_nascimento', 'password1', 'password2', 'tipo_usuario'),
        }),
    )
    
    readonly_fields = ('data_criacao',)

class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'data_publicacao')
    list_filter = ('data_publicacao', 'autor')
    search_fields = ('nome', 'descricao')
    ordering = ('-data_publicacao',)
    
    fieldsets = (
        ('Informações da Notícia', {
            'fields': ('nome', 'descricao', 'imagem', 'autor')
        }),
        ('Informações de Publicação', {
            'fields': ('data_publicacao',)
        }),
    )
    
    readonly_fields = ('data_publicacao',)

class ArtigosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'data_publicacao')
    list_filter = ('data_publicacao', 'autor')
    search_fields = ('nome', 'descricao')
    ordering = ('-data_publicacao',)
    
    fieldsets = (
        ('Informações do Artigo', {
            'fields': ('nome', 'descricao', 'imagem', 'autor')
        }),
        ('Informações de Publicação', {
            'fields': ('data_publicacao',)
        }),
    )
    
    readonly_fields = ('data_publicacao',)

class EditaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'data_publicacao')
    list_filter = ('data_publicacao', 'autor')
    search_fields = ('nome', 'descricao')
    ordering = ('-data_publicacao',)
    
    fieldsets = (
        ('Informações do Edital', {
            'fields': ('nome', 'descricao', 'imagem', 'autor')
        }),
        ('Informações de Publicação', {
            'fields': ('data_publicacao',)
        }),
    )
    
    readonly_fields = ('data_publicacao',)

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('get_comentario_resumo', 'autor', 'data_comentario', 'get_conteudo_relacionado')
    list_filter = ('data_comentario', 'autor')
    search_fields = ('comentario', 'autor__nome_usuario')
    ordering = ('-data_comentario',)
    
    fieldsets = (
        ('Informações do Comentário', {
            'fields': ('autor', 'comentario')
        }),
        ('Conteúdo Relacionado', {
            'fields': ('noticia', 'artigo', 'edital')
        }),
        ('Informações de Publicação', {
            'fields': ('data_comentario',)
        }),
    )
    
    readonly_fields = ('data_comentario',)
    
    def get_comentario_resumo(self, obj):
        if len(obj.comentario) > 50:
            return obj.comentario[:50] + "..."
        return obj.comentario
    get_comentario_resumo.short_description = 'Comentário'
    
    def get_conteudo_relacionado(self, obj):
        if obj.noticia:
            return f"Notícia: {obj.noticia.nome}"
        elif obj.artigo:
            return f"Artigo: {obj.artigo.nome}"
        elif obj.edital:
            return f"Edital: {obj.edital.nome}"
        return "Nenhum conteúdo relacionado"
    get_conteudo_relacionado.short_description = 'Conteúdo Relacionado'

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Artigos, ArtigosAdmin)
admin.site.register(Editais, EditaisAdmin)
admin.site.register(Comentarios, ComentariosAdmin)

admin.site.site_header = "Cultura Mais - Painel Administrativo"
admin.site.site_title = "Cultura Mais Admin"
admin.site.index_title = "Bem-vindo ao painel administrativo do Cultura Mais"