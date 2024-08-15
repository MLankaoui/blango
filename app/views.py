from django.shortcuts import render
from app.models import Infos, ServicesModel, AboutModel


def home(request):
    context = {
        "infos" : Infos.objects.first(),
        "services": ServicesModel.objects.all(),
        "about": AboutModel.objects.first()
    }
    return render(request, 'index.html', context=context)