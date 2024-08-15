from django.shortcuts import render
from app.models import Infos, ServicesModel, AboutModel, Team, ClientsModel


def home(request):
    context = {
        "infos" : Infos.objects.first(),
        "services": ServicesModel.objects.all(),
        "about": AboutModel.objects.first(),
        "team": Team.objects.all(),
        "clients": ClientsModel.objects.all()
    }
    return render(request, 'index.html', context=context)