from django.shortcuts import render


def home(request):
    user = request.user
    if request.user.is_authenticated:
        user = request.user.first_name
    template = 'home.html'
    context = {
        "head_title": "Welcome To My Site",
        "user": user
    }
    return render(request, template, context)


def about(request):
    template = 'about.html'
    context = {
        "head_title": "About Me"
    }
    return render(request, template, context)


def contact(request):
    template = 'contact.html'
    context = {
        "head_title": "Contact Me"
    }
    return render(request, template, context)
