from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from .models import Comentarios, Noticias, Artigos, Editais
from .forms import ComentarioForm

@login_required
def adicionar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            noticia_id = request.POST.get('noticia_id')
            artigo_id = request.POST.get('artigo_id')
            edital_id = request.POST.get('edital_id')
            
            if noticia_id:
                comentario.noticia = get_object_or_404(Noticias, pk=noticia_id)
                redirect_url = 'noticia_detail'
                redirect_pk = noticia_id
            elif artigo_id:
                comentario.artigo = get_object_or_404(Artigos, pk=artigo_id)
                redirect_url = 'artigo_detail'
                redirect_pk = artigo_id
            elif edital_id:
                comentario.edital = get_object_or_404(Editais, pk=edital_id)
                redirect_url = 'edital_detail'
                redirect_pk = edital_id
            else:
                messages.error(request, 'Erro: Conteúdo não identificado.')
                return redirect('home')
            
            if not comentario.comentario.strip():
                messages.error(request, 'O comentário não pode estar vazio.')
                return redirect(redirect_url, pk=redirect_pk)
            
            comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect(redirect_url, pk=redirect_pk)
        else:
            messages.error(request, 'Erro ao adicionar comentário. Verifique os dados.')
    
    return redirect('home')

@login_required
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentarios, pk=comentario_id)
    
    if comentario.autor != request.user and request.user.tipo_usuario != 1:
        return HttpResponseForbidden("Você não tem permissão para editar este comentário.")
    
    if request.method == 'POST':
        novo_comentario = request.POST.get('comentario', '').strip()
        
        if not novo_comentario:
            messages.error(request, 'O comentário não pode estar vazio.')
        else:
            comentario.comentario = novo_comentario
            comentario.save()
            messages.success(request, 'Comentário editado com sucesso!')
        
        if comentario.noticia:
            return redirect('noticia_detail', pk=comentario.noticia.pk)
        elif comentario.artigo:
            return redirect('artigo_detail', pk=comentario.artigo.pk)
        elif comentario.edital:
            return redirect('edital_detail', pk=comentario.edital.pk)
    
    context = {
        'comentario': comentario,
        'form': ComentarioForm(instance=comentario)
    }
    return render(request, 'core/editar_comentario.html', context)

@login_required
def remover_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentarios, pk=comentario_id)
    
    if comentario.autor != request.user and request.user.tipo_usuario != 1:
        return HttpResponseForbidden("Você não tem permissão para remover este comentário.")
    
    if request.method == 'POST':
        if comentario.noticia:
            redirect_url = 'noticia_detail'
            redirect_pk = comentario.noticia.pk
        elif comentario.artigo:
            redirect_url = 'artigo_detail'
            redirect_pk = comentario.artigo.pk
        elif comentario.edital:
            redirect_url = 'edital_detail'
            redirect_pk = comentario.edital.pk
        else:
            redirect_url = 'home'
            redirect_pk = None
        
        comentario.delete()
        
        messages.success(request, 'Comentário removido com sucesso!')
        
        if redirect_pk:
            return redirect(redirect_url, pk=redirect_pk)
        else:
            return redirect(redirect_url)
    
    context = {
        'comentario': comentario
    }
    return render(request, 'core/confirmar_remocao_comentario.html', context)

def listar_comentarios_usuario(request, usuario_id):
    if request.user.tipo_usuario != 1:  
        return HttpResponseForbidden("Acesso negado.")
    
    comentarios = Comentarios.objects.filter(autor_id=usuario_id).order_by('-data_comentario')
    context = {
        'comentarios': comentarios
    }
    return render(request, 'core/comentarios_usuario.html', context)

@login_required
def comentario_ajax_edit(request, comentario_id):
    if request.method == 'POST':
        comentario = get_object_or_404(Comentarios, pk=comentario_id)
        
        if comentario.autor != request.user and request.user.tipo_usuario != 1:
            return JsonResponse({'success': False, 'error': 'Sem permissão'})
        
        novo_comentario = request.POST.get('comentario', '').strip()
        
        if not novo_comentario:
            return JsonResponse({'success': False, 'error': 'Comentário não pode estar vazio'})
        
        comentario.comentario = novo_comentario
        comentario.save()
        
        return JsonResponse({
            'success': True, 
            'comentario': comentario.comentario,
            'data_comentario': comentario.data_comentario.strftime('%d/%m/%Y %H:%M')
        })
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})

@login_required
def comentario_ajax_delete(request, comentario_id):
    if request.method == 'POST':
        comentario = get_object_or_404(Comentarios, pk=comentario_id)
        
        if comentario.autor != request.user and request.user.tipo_usuario != 1:
            return JsonResponse({'success': False, 'error': 'Sem permissão'})
        
        comentario.delete()  
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})

