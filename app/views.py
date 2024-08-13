from django.shortcuts import render
from app.models import Infos


def home(request):
    context = {
        "infos" : Infos.objects.first()
    }
    return render(request, 'index.html', context=context)