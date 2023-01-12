from math import floor
from django.shortcuts import render, redirect
from .forms import NewUserForm, ListaDeQuestoes
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from . import geraPDF
import io
from .models import Stats


def homepage(request):
    if request.user.is_anonymous:
        return render(request=request, template_name='main/index.html')
    stats, created = Stats.objects.get_or_create(
        user=request.user.username)

    emblema = None
    if stats.questoes_completas > 1:
        emblema = 'bronze'
    if stats.questoes_completas > 3:
        emblema = 'prata'
    if stats.questoes_completas > 6:
        emblema = 'ouro'

    context = {
        'username': request.user.username,
        'n': stats.listas_completas,
        'q': stats.questoes_completas,
        'lvl': floor(stats.questoes_completas/100),
        'emblema': emblema
    }
    return render(request=request, template_name='main/index.html', context=context)


@login_required
def sucesso(request):
    choices = geraPDF.get_temas()
    if request.method == "GET":
        form = ListaDeQuestoes(choices=choices)

        context = {
            'form': form,
        }
        return render(request, 'main/sucesso.html', context=context)
    else:
        form = ListaDeQuestoes(data=request.POST, choices=choices)

        if form.is_valid():
            data = {tema: form.cleaned_data.get(
                tema) for tema, maxno in choices}

            buffer = io.BytesIO()
            geraPDF.gerarPDF(data, buffer)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=lista_personalizada.pdf'
            response.write(buffer.getvalue())
            buffer.close()

            stats, created = Stats.objects.get_or_create(
                user=request.user.username)
            stats.listas_completas += 1
            stats.questoes_completas += sum(list(data.values()))
            stats.save()

            return response
        else:
            form = ListaDeQuestoes(choices=choices)

            context = {
                'form': form,
            }
            return render(request, 'main/sucesso.html', context=context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Stats.objects.create(user=user.username)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:login")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:sucesso")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")
