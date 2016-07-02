
from django.shortcuts import render
from models import User, Route


def index(request):
    users = User.objects.all()

    return render(request, "route/index.html", context={'users': users})


def usermap(request):
    filter_from_options = ["Point A", "Point A2"]
    if 'filter_from' in request.POST:
        # return filter_to
        filter_from = request.POST['filter_from']
        route = Route.objects.filter(route_id=filter_from)
        route_field_type = route.get('field_type')
        if route_field_type == 'Point A':
            routes = Route.objects.filter(field_type="Point A2")
        else:
            routes = Route.objects.filter(field_type="Station")
        context = {'filter_to': routes}
    else:
        # return filter_from
        routes = Route.objects.filter(field_type__in=filter_from_options)
        context = {'filter_from': routes}
    context = {'from_filter': ['KTM', 'PKR'], 'to_filter': ["BHW", "NGJ", "DNG", "SURK", "BRT"]}
    return render(request, 'route/usermap.html', context=context)
