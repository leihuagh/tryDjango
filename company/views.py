from django.shortcuts import render


def home(request):
    user = request.user
    if request.user.is_authenticated:
        user = request.user.first_name
    template = 'home.html'
    context = {
        "user": user
    }
    return render(request, template, context)
