from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print("HELLO WORLD")
    return render(request, "base.html")
