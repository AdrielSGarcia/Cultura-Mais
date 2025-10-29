from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Noticias, Artigos, Editais
from django import forms

def is_admin(user):
    return user.is_authenticated and user.tipo_usuario == 1

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['nome', 'descricao', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título da notícia'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Conteúdo da notícia'
            }),
            'imagem': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigos
        fields = ['nome', 'descricao', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do artigo'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Conteúdo do artigo'
            }),
            'imagem': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

class EditalForm(forms.ModelForm):
    class Meta:
        model = Editais
        fields = ['nome', 'descricao', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do edital'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Conteúdo do edital'
            }),
            'imagem': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

@user_passes_test(is_admin)
def criar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            if not form.cleaned_data['nome'].strip():
                messages.error(request, 'O título da notícia é obrigatório.')
                return render(request, 'core/criar_noticia.html', {'form': form})
            
            if not form.cleaned_data['descricao'].strip():
                messages.error(request, 'O conteúdo da notícia é obrigatório.')
                return render(request, 'core/criar_noticia.html', {'form': form})
            
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            messages.success(request, 'Notícia criada com sucesso!')
            return redirect('noticia_detail', pk=noticia.pk)
        else:
            messages.error(request, 'Erro ao criar notícia. Verifique os dados.')
    else:
        form = NoticiaForm()
    
    return render(request, 'core/criar_noticia.html', {'form': form})

@user_passes_test(is_admin)
def criar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            if not form.cleaned_data['nome'].strip():
                messages.error(request, 'O título do artigo é obrigatório.')
                return render(request, 'core/criar_artigo.html', {'form': form})
            
            if not form.cleaned_data['descricao'].strip():
                messages.error(request, 'O conteúdo do artigo é obrigatório.')
                return render(request, 'core/criar_artigo.html', {'form': form})
            
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            messages.success(request, 'Artigo criado com sucesso!')
            return redirect('artigo_detail', pk=artigo.pk)
        else:
            messages.error(request, 'Erro ao criar artigo. Verifique os dados.')
    else:
        form = ArtigoForm()
    
    return render(request, 'core/criar_artigo.html', {'form': form})

@user_passes_test(is_admin)
def criar_edital(request):
    if request.method == 'POST':
        form = EditalForm(request.POST, request.FILES)
        if form.is_valid():
            if not form.cleaned_data['nome'].strip():
                messages.error(request, 'O título do edital é obrigatório.')
                return render(request, 'core/criar_edital.html', {'form': form})
            
            if not form.cleaned_data['descricao'].strip():
                messages.error(request, 'O conteúdo do edital é obrigatório.')
                return render(request, 'core/criar_edital.html', {'form': form})
            
            edital = form.save(commit=False)
            edital.autor = request.user
            edital.save()
            messages.success(request, 'Edital criado com sucesso!')
            return redirect('edital_detail', pk=edital.pk)
        else:
            messages.error(request, 'Erro ao criar edital. Verifique os dados.')
    else:
        form = EditalForm()
    
    return render(request, 'core/criar_edital.html', {'form': form})

@user_passes_test(is_admin)
def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            if not form.cleaned_data['nome'].strip():
                messages.error(request, 'O título da notícia é obrigatório.')
                return render(request, 'core/editar_noticia.html', {'form': form, 'noticia': noticia})
            
            if not form.cleaned_data['descricao'].strip():
                messages.error(request, 'O conteúdo da notícia é obrigatório.')
                return render(request, 'core/editar_noticia.html', {'form': form, 'noticia': noticia})
            
            form.save()
            messages.success(request, 'Notícia editada com sucesso!')
            return redirect('noticia_detail', pk=noticia.pk)
        else:
            messages.error(request, 'Erro ao editar notícia. Verifique os dados.')
    else:
        form = NoticiaForm(instance=noticia)
    
    return render(request, 'core/editar_noticia.html', {'form': form, 'noticia': noticia})

@user_passes_test(is_admin)
def editar_artigo(request, pk):
    artigo = get_object_or_404(Artigos, pk=pk)
    
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            if not form.cleaned_data['nome'].strip():
                messages.error(request, 'O título do artigo é obrigatório.')
                return render(request, 'core/editar_artigo.html', {'form': form, 'artigo': artigo})
            
            if not form.cleaned_data['descricao'].strip():
                messages.error(request, 'O conteúdo do artigo é obrigatório.')
                return render(request, 'core/editar_artigo.html', {'form': form, 'artigo': artigo})
            
            form.save()
            messages.success(request, 'Artigo editado com sucesso!')
            return redirect('artigo_detail', pk=artigo.pk)
        else:
            messages.error(request, 'Erro ao editar artigo. Verifique os dados.')
    else:
        form = ArtigoForm(instance=artigo)
    
    return render(request, 'core/editar_artigo.html', {'form': form, 'artigo': artigo})

@user_passes_test(is_admin)
def editar_edital(request, pk):
    edital = get_object_or_404(Editais, pk=pk)
    
    if request.method == 'POST':
        form = EditalForm(request.POST, request.FILES, instance=edital)
        if form.is_valid():
            if not form.cleaned_data['nome'].strip():
                messages.error(request, 'O título do edital é obrigatório.')
                return render(request, 'core/editar_edital.html', {'form': form, 'edital': edital})
            
            if not form.cleaned_data['descricao'].strip():
                messages.error(request, 'O conteúdo do edital é obrigatório.')
                return render(request, 'core/editar_edital.html', {'form': form, 'edital': edital})
            
            form.save()
            messages.success(request, 'Edital editado com sucesso!')
            return redirect('edital_detail', pk=edital.pk)
        else:
            messages.error(request, 'Erro ao editar edital. Verifique os dados.')
    else:
        form = EditalForm(instance=edital)
    
    return render(request, 'core/editar_edital.html', {'form': form, 'edital': edital})

@user_passes_test(is_admin)
def remover_noticia(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    
    if request.method == 'POST':
        noticia.delete()  
        messages.success(request, 'Notícia removida com sucesso!')
        return redirect('noticia_list')
    
    return render(request, 'core/confirmar_remocao_noticia.html', {'noticia': noticia})

@user_passes_test(is_admin)
def remover_artigo(request, pk):
    artigo = get_object_or_404(Artigos, pk=pk)
    
    if request.method == 'POST':
        artigo.delete()
        messages.success(request, 'Artigo removido com sucesso!')
        return redirect('artigo_list')
    
    return render(request, 'core/confirmar_remocao_artigo.html', {'artigo': artigo})

@user_passes_test(is_admin)
def remover_edital(request, pk):
    edital = get_object_or_404(Editais, pk=pk)
    
    if request.method == 'POST':
        edital.delete()
        messages.success(request, 'Edital removido com sucesso!')
        return redirect('edital_list')
    
    return render(request, 'core/confirmar_remocao_edital.html', {'edital': edital})

@user_passes_test(is_admin)
def gerenciar_conteudo(request):
    noticias = Noticias.objects.all().order_by('-data_publicacao')[:10]
    artigos = Artigos.objects.all().order_by('-data_publicacao')[:10]
    editais = Editais.objects.all().order_by('-data_publicacao')[:10]
    
    context = {
        'noticias': noticias,
        'artigos': artigos,
        'editais': editais,
    }
    return render(request, 'core/gerenciar_conteudo.html', context)

