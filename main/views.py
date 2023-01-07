from math import floor
from django.shortcuts import render, redirect
from .forms import NewUserForm, ListaDeQuestoes
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http.response import HttpResponse
from . import geraPDF
import io
from .models import Stats


def homepage(request):
    return render(request=request, template_name='main/index.html')


def sucesso(request):
    if request.method == "GET":
        form = ListaDeQuestoes()
        context = {
            'form': form,
            'username': request.user.username,
            'n': Stats.objects.get(user=request.user.username).listas_completas,
            'q': Stats.objects.get(user=request.user.username).questoes_completas,
            'lvl': floor(Stats.objects.get(user=request.user.username).questoes_completas/100)
        }
        return render(request, 'main/sucesso.html', context=context)
    else:
        form = ListaDeQuestoes(request.POST)

        if form.is_valid():
            quant = form.cleaned_data.get('quant')
            tema = form.cleaned_data.get('tema')

            buffer = io.BytesIO()
            geraPDF.gerarPDF(tema, quant, buffer)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=lista_personalizada.pdf'
            response.write(buffer.getvalue())
            buffer.close()

            form = ListaDeQuestoes()

        stats = Stats.objects.get(user=request.user.username)
        stats.listas_completas += 1
        stats.questoes_completas += quant
        stats.save()

        return response


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


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")
