from django.shortcuts import redirect


def index(request):
    # didn't create template for it.
    return redirect('/route/')
