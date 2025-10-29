from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ComentarioForm
from .models import Noticias, Artigos, Editais, Comentarios

def home(request):
    # Página inicial com as últimas postagens de todas as categorias
    noticias = Noticias.objects.all().order_by("-data_publicacao")[:3]
    artigos = Artigos.objects.all().order_by("-data_publicacao")[:3]
    editais = Editais.objects.all().order_by("-data_publicacao")[:3]
    
    context = {
        'noticias': noticias,
        'artigos': artigos,
        'editais': editais,
    }
    return render(request, "core/home.html", context)

def noticia_list(request):
    noticias = Noticias.objects.all().order_by("-data_publicacao")
    return render(request, "core/noticia_list.html", {"noticias": noticias})

def noticia_detail(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    comentarios = noticia.comentarios.all().order_by("-data_comentario")
    form = ComentarioForm()
    return render(request, "core/noticia_detail.html", {"noticia": noticia, "comentarios": comentarios, "form": form})

def artigo_list(request):
    artigos = Artigos.objects.all().order_by("-data_publicacao")
    return render(request, "core/artigo_list.html", {"artigos": artigos})

def artigo_detail(request, pk):
    artigo = get_object_or_404(Artigos, pk=pk)
    comentarios = artigo.comentarios.all().order_by("-data_comentario")
    form = ComentarioForm()
    return render(request, "core/artigo_detail.html", {"artigo": artigo, "comentarios": comentarios, "form": form})

def edital_list(request):
    editais = Editais.objects.all().order_by("-data_publicacao")
    return render(request, "core/edital_list.html", {"editais": editais})

def edital_detail(request, pk):
    edital = get_object_or_404(Editais, pk=pk)
    comentarios = edital.comentarios.all().order_by("-data_comentario")
    form = ComentarioForm()
    return render(request, "core/edital_detail.html", {"edital": edital, "comentarios": comentarios, "form": form})



@login_required
def add_comment_to_noticia(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect("noticia_detail", pk=noticia.pk)
        else:
            messages.error(request, 'Erro ao adicionar comentário. Verifique os dados.')
    return redirect("noticia_detail", pk=noticia.pk)

@login_required
def add_comment_to_artigo(request, pk):
    artigo = get_object_or_404(Artigos, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect("artigo_detail", pk=artigo.pk)
        else:
            messages.error(request, 'Erro ao adicionar comentário. Verifique os dados.')
    return redirect("artigo_detail", pk=artigo.pk)

@login_required
def add_comment_to_edital(request, pk):
    edital = get_object_or_404(Editais, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.edital = edital
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect("edital_detail", pk=edital.pk)
        else:
            messages.error(request, 'Erro ao adicionar comentário. Verifique os dados.')
    return redirect("edital_detail", pk=edital.pk)

