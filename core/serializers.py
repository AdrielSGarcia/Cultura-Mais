from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Noticias, Artigos, Editais, Comentarios

# --- User Serializers (sem alterações) ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password_confirm']
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return attrs
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user

# --- CORREÇÃO: Serializers de Conteúdo ---
# Adicionei 'source' para renomear os campos 'nome' e 'descricao' para 'titulo' e 'conteudo' na saída da API.
# Também adicionei 'comentarios_count' que o frontend utiliza.

class NoticiaSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(source='nome')
    conteudo = serializers.CharField(source='descricao')
    comentarios_count = serializers.SerializerMethodField()

    class Meta:
        model = Noticias
        fields = ['id_noticia', 'titulo', 'conteudo', 'autor', 'data_publicacao', 'imagem', 'comentarios_count']

    def get_comentarios_count(self, obj):
        return obj.comentarios.count()

class ArtigoSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(source='nome')
    conteudo = serializers.CharField(source='descricao')
    comentarios_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Artigos
        fields = ['id_artigo', 'titulo', 'conteudo', 'autor', 'data_publicacao', 'imagem', 'comentarios_count']

    def get_comentarios_count(self, obj):
        return obj.comentarios.count()
        
class EditalSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(source='nome')
    conteudo = serializers.CharField(source='descricao')
    comentarios_count = serializers.SerializerMethodField()

    class Meta:
        model = Editais
        fields = ['id_edital', 'titulo', 'conteudo', 'autor', 'data_publicacao', 'imagem', 'comentarios_count']
        
    def get_comentarios_count(self, obj):
        return obj.comentarios.count()

# --- Comentario Serializers (sem alterações) ---
class ComentarioSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)
    class Meta:
        model = Comentarios
        fields = ['id_comentario', 'comentario', 'autor', 'data_comentario', 'noticia', 'artigo', 'edital']
        read_only_fields = ['id_comentario', 'autor', 'data_comentario']

class ComentarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ['comentario'] # Simplificado, o conteúdo é associado na view

# --- Home Serializer (sem alterações) ---
class HomeDataSerializer(serializers.Serializer):
    ultimas_noticias = NoticiaSerializer(many=True, read_only=True)
    ultimos_artigos = ArtigoSerializer(many=True, read_only=True)
    ultimos_editais = EditalSerializer(many=True, read_only=True)
