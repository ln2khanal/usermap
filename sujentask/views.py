from django.http import HttpResponse


def index(request):
    # didn't create template for it.
    return HttpResponse("<center>Working!<br/>Jump to /route/</center>")
