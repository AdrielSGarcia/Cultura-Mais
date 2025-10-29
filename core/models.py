# Modelos do sistema Cultura Mais
# Este arquivo contém todos os modelos (tabelas do banco de dados) do nosso sistema
# Seguindo o diagrama de classes fornecido na documentação

from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, help_text="CPF do usuário (11 dígitos)")
    nome = models.CharField(max_length=200, help_text="Nome completo do usuário")
    email = models.EmailField(unique=True, help_text="Email do usuário")
    nome_usuario = models.CharField(max_length=150, unique=True, help_text="Nome de usuário para fazer login")
    tipo_usuario = models.IntegerField(default=0, help_text="Tipo: 0=Usuário comum, 1=Administrador")
    data_nascimento = models.DateField(default=date.today, help_text="Data de nascimento do usuário")
    data_criacao = models.DateTimeField(auto_now_add=True, help_text="Data de criação da conta")
    
    username = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return self.nome_usuario
    
    def get_cpf(self):
        return self.cpf
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
    
    def get_nome_usuario(self):
        return self.nome_usuario
    
    def set_nome_usuario(self, nome_usuario):
        self.nome_usuario = nome_usuario
    
    def get_data_nascimento(self):
        return self.data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento
    
    def get_tipo_usuario(self):
        return self.tipo_usuario
    
    def set_tipo_usuario(self, tipo_usuario):
        self.tipo_usuario = tipo_usuario
    
    def get_data_criacao(self):
        return self.data_criacao

class Noticias(models.Model):
    class Meta:
        verbose_name_plural = "Notícias"
    id_noticia = models.AutoField(primary_key=True)  # ID único da notícia
    nome = models.CharField(max_length=200, help_text="Título da notícia")
    descricao = models.TextField(help_text="Conteúdo completo da notícia")
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True, help_text="Imagem da notícia (opcional)")
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, help_text="Usuário que criou a notícia")
    data_publicacao = models.DateTimeField(auto_now_add=True)  # Data é preenchida automaticamente
    
    def __str__(self):
        return self.nome

    def get_id(self):
        return self.id_noticia
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_descricao(self):
        return self.descricao
    
    def set_descricao(self, descricao):
        self.descricao = descricao
    
    def get_autor(self):
        return self.autor
    
    def set_autor(self, autor):
        self.autor = autor
    
    def get_imagem(self):
        return self.imagem
    
    def set_imagem(self, imagem):
        self.imagem = imagem

class Artigos(models.Model):
    class Meta:
        verbose_name_plural = "Artigos"
    id_artigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, help_text="Título do artigo")
    descricao = models.TextField(help_text="Conteúdo completo do artigo")
    imagem = models.ImageField(upload_to='artigos/', blank=True, null=True, help_text="Imagem do artigo (opcional)")
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, help_text="Usuário que criou o artigo")
    data_publicacao = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.nome
    
    def get_id(self):
        return self.id_artigo
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_descricao(self):
        return self.descricao
    
    def set_descricao(self, descricao):
        self.descricao = descricao
    
    def get_autor(self):
        return self.autor
    
    def set_autor(self, autor):
        self.autor = autor
    
    def get_imagem(self):
        return self.imagem
    
    def set_imagem(self, imagem):
        self.imagem = imagem

class Editais(models.Model):
    class Meta:
        verbose_name_plural = "Editais"
    id_edital = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, help_text="Título do edital")
    descricao = models.TextField(help_text="Conteúdo do edital")
    imagem = models.ImageField(upload_to='editais/', blank=True, null=True, help_text="Imagem do edital")
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, help_text="Autor do edital")
    data_publicacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    def get_id(self):
        return self.id_edital
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_descricao(self):
        return self.descricao
    
    def set_descricao(self, descricao):
        self.descricao = descricao
    
    def get_autor(self):
        return self.autor
    
    def set_autor(self, autor):
        self.autor = autor
    
    def get_imagem(self):
        return self.imagem
    
    def set_imagem(self, imagem):
        self.imagem = imagem

class Comentarios(models.Model):
    class Meta:
        verbose_name_plural = "Comentários"
    id_comentario = models.AutoField(primary_key=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, help_text="Autor do comentário")
    comentario = models.TextField(help_text="Texto do comentário")
    data_comentario = models.DateTimeField(auto_now_add=True, help_text="Data do comentário")
    
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, null=True, blank=True, related_name='comentarios')
    artigo = models.ForeignKey(Artigos, on_delete=models.CASCADE, null=True, blank=True, related_name='comentarios')
    edital = models.ForeignKey(Editais, on_delete=models.CASCADE, null=True, blank=True, related_name='comentarios')
    
    def __str__(self):
        return f"Comentário por {self.autor.nome_usuario} em {self.data_comentario.strftime('%Y-%m-%d %H:%M')}"
    
    def get_id(self):
        return self.id_comentario
    
    def get_autor(self):
        return self.autor
    
    def get_comentario(self):
        return self.comentario
    
    def set_comentario(self, comentario):
        self.comentario = comentario
    
    def get_data_comentario(self):
        return self.data_comentario

