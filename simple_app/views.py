import datetime
import os
import logging

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from simple_app.forms import SignUpForm, CreateGameForm
from simple_app.models import Game


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def index(request):
    return render(request, 'simple_app/index.html', {
        'username': request.user.username if not request.user.is_anonymous else "somebody",
    })


def profile(request):
    return render(request, 'registration/profile.html', {
        'user': request.user if not request.user.is_anonymous else None,
    })


def games(request):
    return render(request, 'simple_app/games.html', {
        'username': request.user.username if not request.user.is_anonymous else "somebody",
        'games': Game.objects.all(),
    })


def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateGameForm()
    return render(request, 'simple_app/create_game.html', {
        'form': form,
        'user': request.user if not request.user.is_anonymous else None,
    })
