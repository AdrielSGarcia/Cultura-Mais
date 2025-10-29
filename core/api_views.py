from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Noticias, Artigos, Editais, Comentarios, Usuario
from .serializers import (
    NoticiaSerializer, ArtigoSerializer, EditalSerializer, 
    ComentarioSerializer, ComentarioCreateSerializer,
    UserSerializer, UserRegistrationSerializer, HomeDataSerializer
)


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticias.objects.all().order_by('-data_publicacao')
    serializer_class = NoticiaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

    @action(detail=True, methods=['get'])
    def comentarios(self, request, pk=None):
        noticia = self.get_object()
        comentarios = noticia.comentarios.all().order_by('-data_publicacao')
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def adicionar_comentario(self, request, pk=None):
        noticia = self.get_object()
        serializer = ComentarioCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(autor=request.user, noticia=noticia)
            return Response(
                ComentarioSerializer(serializer.instance).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigos.objects.all().order_by('-data_publicacao')
    serializer_class = ArtigoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

    @action(detail=True, methods=['get'])
    def comentarios(self, request, pk=None):
        artigo = self.get_object()
        comentarios = artigo.comentarios.all().order_by('-data_publicacao')
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def adicionar_comentario(self, request, pk=None):
        artigo = self.get_object()
        serializer = ComentarioCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(autor=request.user, artigo=artigo)
            return Response(
                ComentarioSerializer(serializer.instance).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditalViewSet(viewsets.ModelViewSet):
    queryset = Editais.objects.all().order_by('-data_publicacao')
    serializer_class = EditalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

    @action(detail=True, methods=['get'])
    def comentarios(self, request, pk=None):
        edital = self.get_object()
        comentarios = edital.comentarios.all().order_by('-data_publicacao')
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def adicionar_comentario(self, request, pk=None):
        edital = self.get_object()
        serializer = ComentarioCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(autor=request.user, edital=edital)
            return Response(
                ComentarioSerializer(serializer.instance).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all().order_by('-data_comentario')
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        
        noticia_id = self.request.query_params.get('noticia', None)
        artigo_id = self.request.query_params.get('artigo', None)
        edital_id = self.request.query_params.get('edital', None)
        
        if noticia_id is not None:
            queryset = queryset.filter(noticia_id=noticia_id)
        elif artigo_id is not None:
            queryset = queryset.filter(artigo_id=artigo_id)
        elif edital_id is not None:
            queryset = queryset.filter(edital_id=edital_id)
            
        return queryset

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)


class HomeDataView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        ultimas_noticias = Noticias.objects.all().order_by('-data_publicacao')[:3]
        ultimos_artigos = Artigos.objects.all().order_by('-data_publicacao')[:3]
        ultimos_editais = Editais.objects.all().order_by('-data_publicacao')[:3]

        data = {
            'ultimas_noticias': NoticiaSerializer(ultimas_noticias, many=True).data,
            'ultimos_artigos': ArtigoSerializer(ultimos_artigos, many=True).data,
            'ultimos_editais': EditalSerializer(ultimos_editais, many=True).data,
        }

        return Response(data)


class AuthView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': UserSerializer(user).data
                })
            else:
                return Response(
                    {'error': 'Credenciais inválidas'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
        else:
            return Response(
                {'error': 'Username e password são obrigatórios'}, 
                status=status.HTTP_400_BAD_REQUEST
            )


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data,
                'message': 'Usuário criado com sucesso!'
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        query = request.query_params.get('q', '')
        
        if not query:
            return Response({'error': 'Parâmetro de busca é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)

        noticias = Noticias.objects.filter(
            Q(nome__icontains=query) | Q(descricao__icontains=query)
        ).order_by('-data_publicacao')[:5]

        artigos = Artigos.objects.filter(
            Q(nome__icontains=query) | Q(descricao__icontains=query)
        ).order_by('-data_publicacao')[:5]

        editais = Editais.objects.filter(
            Q(nome__icontains=query) | Q(descricao__icontains=query)
        ).order_by('-data_publicacao')[:5]

        data = {
            'query': query,
            'noticias': NoticiaSerializer(noticias, many=True).data,
            'artigos': ArtigoSerializer(artigos, many=True).data,
            'editais': EditalSerializer(editais, many=True).data,
        }

        return Response(data)
    
class LogoutView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"detail": "Logout successful."},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": "Invalid token or token not provided."},
                status=status.HTTP_400_BAD_REQUEST
            )

