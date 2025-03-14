from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from .forms import UsuarioCreationForm, PreferenciasForm
from .models import Usuario, Preferencias
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def cadastrar(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')

            username = user_form.email
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(
                    request,
                    "Cadastro realizado com sucesso! Você foi autenticado automaticamente.",
                )
                return redirect("selecionar_restaurante")
            else:
                messages.error(request, "Erro ao autenticar o usuário após o cadastro.")

            return redirect('selecionar_restaurante')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados e tente novamente.')
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuario/cadastrar.html', {'form': form})


def logar_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('selecionar_restaurante')
        else:
            messages.error(request, 'E-mail ou senha incorretos. Tente novamente.')
    return render(request, 'usuario/login.html')


def esqueci_senha(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            email = password_reset_form.cleaned_data['email']
            associated_users = Usuario.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = 'Redefinição de senha solicitada'
                    email_template_name = 'password_reset_email.html'
                    # context = {
                    #     "email": user.email,
                    #     'domain': settings.DOMAIN,
                    #     'site_name': 'Seu Site',
                    #     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    #     "user": user,
                    #     'token': default_token_generator.make_token(user),
                    #     'protocol': 'http',
                    # }
                    # email_message = render_to_string(email_template_name, context)
                    # send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [user.email])
                    messages.success(request, 'Instruções de redefinição de senha enviadas para o seu e-mail.')
                    return redirect('logar_usuario')
            else:
                messages.error(request, 'Nenhum usuário associado a esse e-mail.')
    password_reset_form = PasswordResetForm()
    return render(request, 'usuario/esqueci_senha.html', {'password_reset_form': password_reset_form})


@login_required
def definir_preferencias_alimentares(request):
    preferencias, created = Preferencias.objects.get_or_create(usuario=request.user)

    if request.method == "POST":
        form = PreferenciasForm(request.POST, instance=preferencias)
        if form.is_valid():
            form.save()
            return redirect("ver_agendamentos")
    else:
        form = PreferenciasForm(instance=preferencias)

    return render(request, "usuario/definir_preferencias.html", {"form": form})

def index(request):
    if request.user.is_authenticated:
        return redirect('selecionar_restaurante')
    else:
        return render(request, 'usuario/index.html')

def logout_view(request):
    logout(request)
    return redirect("login")
