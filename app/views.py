from django.shortcuts import redirect, render
from app.models import Infos, ServicesModel, AboutModel, Team, ClientsModel
from app.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Process the form data (e.g., send an email)
            send_mail(
                f"Contact Form Submission from {name}",
                message,
                email,  # From email
                ['your_email@example.com'],  # To email
                fail_silently=False,
            )

            # Redirect to the success page
            return redirect('success')
    else:
        form = ContactForm()
    
    context = {
        "infos": Infos.objects.first(),
        "services": ServicesModel.objects.all(),
        "about": AboutModel.objects.first(),
        "team": Team.objects.all(),
        "clients": ClientsModel.objects.all(),
        "form": form,
    }
    return render(request, 'index.html', context=context)


def success(request):
    return HttpResponse('Success! Your message has been sent.')
