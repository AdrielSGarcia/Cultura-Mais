from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

try:
    from .api_views_simples import (
        NoticiasAPIViewSet, ArtigosAPIViewSet, EditaisAPIViewSet, 
        ComentariosAPIViewSet, DadosHomeAPIView, busca_geral_api, estatisticas_api
    )
except ImportError:
    NoticiasAPIViewSet = None
    ArtigosAPIViewSet = None
    EditaisAPIViewSet = None
    ComentariosAPIViewSet = None
    DadosHomeAPIView = None
    busca_geral_api = None
    estatisticas_api = None

router = DefaultRouter()

if NoticiasAPIViewSet:
    router.register(r'noticias', NoticiasAPIViewSet)
if ArtigosAPIViewSet:
    router.register(r'artigos', ArtigosAPIViewSet)
if EditaisAPIViewSet:
    router.register(r'editais', EditaisAPIViewSet)
if ComentariosAPIViewSet:
    router.register(r'comentarios', ComentariosAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if DadosHomeAPIView:
    urlpatterns.append(path('home/', DadosHomeAPIView.as_view(), name='api-home'))
if busca_geral_api:
    urlpatterns.append(path('busca/', busca_geral_api, name='api-busca'))
if estatisticas_api:
    urlpatterns.append(path('estatisticas/', estatisticas_api, name='api-estatisticas'))

