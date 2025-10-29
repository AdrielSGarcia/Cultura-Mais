# Views de autenticação para o sistema Cultura Mais
# Implementando os requisitos RF04 (Autenticação) e RF05 (Cadastro de Usuário)

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django import forms
from .models import Usuario

class UsuarioCadastroForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )
    password2 = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'})
    )

    class Meta:
        model = Usuario
        fields = ('nome', 'nome_usuario', 'cpf', 'email', 'data_nascimento')
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo'
            }),
            'nome_usuario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário para login'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CPF (apenas números)',
                'maxlength': '11'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            cpf = ''.join(filter(str.isdigit, cpf))
            if len(cpf) != 11:
                raise forms.ValidationError("CPF deve ter 11 dígitos.")
            if Usuario.objects.filter(cpf=cpf).exists():
                raise forms.ValidationError("Este CPF já está cadastrado.")
        return cpf

    def clean_nome_usuario(self):
        nome_usuario = self.cleaned_data.get('nome_usuario')
        if Usuario.objects.filter(nome_usuario=nome_usuario).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return nome_usuario

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["nome_usuario"]  # Django precisa do username
        user.set_password(self.cleaned_data["password1"])
        user.tipo_usuario = 0  # Usuário comum por padrão
        if commit:
            user.save()
        return user

def cadastro_usuario_view(request):
    if request.method == 'POST':
        form = UsuarioCadastroForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, f'Conta criada para {user.nome}! Você já pode fazer login.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Erro ao criar conta: {str(e)}')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados informados.')
    else:
        form = UsuarioCadastroForm()
    
    return render(request, 'registration/register.html', {'form': form})

class AutenticacaoLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Bem-vindo, {user.nome or user.nome_usuario}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Nome de usuário ou senha incorretos.')
        return super().form_invalid(form)

class AutenticacaoLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, f'Até logo, {request.user.nome or request.user.nome_usuario}!')
        return super().dispatch(request, *args, **kwargs)

def autenticar_usuario(nome_usuario, senha):
    try:
        user = authenticate(username=nome_usuario, password=senha)
        return user
    except Exception:
        return None

def cadastrar_usuario(cpf, nome, email, nome_usuario, senha, data_nascimento):
    try:
        user = Usuario.objects.create_user(
            username=nome_usuario,
            nome_usuario=nome_usuario,
            nome=nome,
            email=email,
            cpf=cpf,
            data_nascimento=data_nascimento,
            password=senha
        )
        return user
    except Exception as e:
        raise Exception(f"Erro ao cadastrar usuário: {str(e)}")

