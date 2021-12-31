import os

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

import logging


def index(request):
    return render(request, 'simple_app/index.html', {
        'username': request.user.username if not request.user.is_anonymous else "somebody",
    })


def profile(request):
    return render(request, 'registration/profile.html', {
        'user': request.user if not request.user.is_anonymous else None,
    })
