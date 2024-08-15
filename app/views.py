from django.shortcuts import render
from app.models import Infos, ServicesModel


def home(request):
    context = {
        "infos" : Infos.objects.first(),
        "services": ServicesModel.objects.all()
    }
    return render(request, 'index.html', context=context)