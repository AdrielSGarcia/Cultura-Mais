from django import forms
from .models import Comentarios, Usuario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ("comentario",)
        widgets = {
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Digite seu comentário aqui...'
            })
        }

class FormularioComentario(forms.ModelForm):
    """
    Este formulário é usado para criar comentários
    Ele é baseado no modelo Comentarios
    """
    
    class Meta:
        # Especificar qual modelo este formulário representa
        model = Comentarios
        
        # Especificar quais campos do modelo queremos no formulário
        # Só queremos o campo 'comentario' porque os outros (autor, data, etc.) 
        # são preenchidos automaticamente
        fields = ("comentario",)
        
        # Definir como os campos vão aparecer na página (widgets)
        widgets = {
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',  # Classe CSS do Bootstrap para estilização
                'rows': 4,  # Número de linhas da caixa de texto
                'placeholder': 'Digite seu comentário aqui...'  # Texto de exemplo
            })
        }

class FormularioCadastroUsuario(forms.ModelForm):
    """
    Este formulário é usado para cadastrar novos usuários
    Ele é baseado no modelo Usuario
    """
    
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )
    
    confirmar_senha = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha novamente'
        })
    )
    
    class Meta:
        # Especificar qual modelo este formulário representa
        model = Usuario
        
        # Especificar quais campos do modelo queremos no formulário
        fields = ('nome', 'nome_usuario', 'cpf', 'email', 'data_nascimento')
        
        # Definir como os campos vão aparecer na página (widgets)
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome completo'
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
                'placeholder': 'Seu e-mail'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
    
    def clean_confirmar_senha(self):
        """
        Esta função verifica se as duas senhas são iguais
        """
        senha = self.cleaned_data.get("senha")
        confirmar_senha = self.cleaned_data.get("confirmar_senha")
        
        # Se as senhas existem e são diferentes, mostrar erro
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não são iguais.")
        
        return confirmar_senha
    
    def clean_cpf(self):
        """
        Esta função verifica se o CPF é válido
        """
        cpf = self.cleaned_data.get('cpf')
        
        if cpf:
            # Remover caracteres que não são números
            cpf_apenas_numeros = ''.join(filter(str.isdigit, cpf))
            
            # Verificar se tem 11 dígitos
            if len(cpf_apenas_numeros) != 11:
                raise forms.ValidationError("CPF deve ter 11 dígitos.")
            
            # Verificar se já existe outro usuário com este CPF
            if Usuario.objects.filter(cpf=cpf_apenas_numeros).exists():
                raise forms.ValidationError("Este CPF já está cadastrado.")
        
        return cpf_apenas_numeros
    
    def clean_nome_usuario(self):
        """
        Esta função verifica se o nome de usuário já existe
        """
        nome_usuario = self.cleaned_data.get('nome_usuario')
        
        # Verificar se já existe outro usuário com este nome
        if Usuario.objects.filter(nome_usuario=nome_usuario).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        
        return nome_usuario
    
    def clean_email(self):
        """
        Esta função verifica se o email já existe
        """
        email = self.cleaned_data.get('email')
        
        # Verificar se já existe outro usuário com este email
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        
        return email
    
    def save(self, commit=True):
        """
        Esta função salva o usuário no banco de dados
        """
        # Criar o usuário mas não salvar ainda
        usuario = super().save(commit=False)
        
        # Definir o username (Django precisa deste campo)
        usuario.username = self.cleaned_data["nome_usuario"]
        
        # Definir a senha (criptografada)
        usuario.set_password(self.cleaned_data["senha"])
        
        # Definir como usuário comum (não administrador)
        usuario.tipo_usuario = 0
        
        # Se commit=True, salvar no banco de dados
        if commit:
            usuario.save()
        
        return usuario

class FormularioLogin(forms.Form):
    """
    Este formulário é usado para fazer login
    """
    
    nome_usuario = forms.CharField(
        label='Nome de Usuário',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu nome de usuário'
        })
    )
    
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Sua senha'
        })
    )


