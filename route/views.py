
from models import User, Route
from django.http import JsonResponse
from django.shortcuts import render, redirect

import logging


def index(request):
    """
    :returns a list of users for listing.
    """
    users = User.objects.all()

    return render(request, "route/index.html", context={'users': users})


def usermap(request):
    """
    :returns context for from_filter options for rendering.
    """
    context = {}
    if Route.objects.filter().count() > 0:
        context = {'from_filter': ["Point A", "Point A2"]}

    return render(request, 'route/usermap.html', context=context)


def getdestination(request):
    """
    :returns json response for to_filter options.
    """
    context = {}
    if Route.objects.filter().count() > 0:
        if request.GET['from_filter'] == 'Point A2':
            context = {'to_filter': 'PointA'}
        else:
            context = {'to_filter': "Station"}

    return JsonResponse(context)


def getallroutes(request):
    """
    :returns list of routes for all the users as requested as a json response.

    """
    context = {}
    try:
        assert 'from_filter' in request.GET
        assert 'to_filter' in request.GET
    except Exception as err:
        context['message'] = "Source & Destination not sent in request, ", err
    else:
        src = request.GET['from_filter']
        dst = request.GET['to_filter']
        # JS is sending only Point for the value "Point A"
        if dst == 'PointA':
            dst = 'Point A'
        sources = Route.objects.filter(field_type=src)
        for source in sources:
            destination = Route.objects.filter(field_type=dst, user=source.user)
            if destination.count() == 1:
                destination = destination[0]
                user_context = {
                    "source": {'lat': source.latitude, 'lng': source.longitude},
                    "destination": {'lat': destination.latitude, 'lng': destination.longitude}
                }
                context["%s %s" % (source.user.first_name, source.user.last_name)] = user_context
    finally:
        return JsonResponse(context)


def userroute(request):
    """
    :returns user route info if found otherwise an error message
    """
    context = {}
    try:
        user = request.GET['user']
        source = Route.objects.filter(route_key=user, field_type="Point A")
        destination = Route.objects.filter(route_key=user, field_type="Point A2")
        if destination.count() == 1:
            context['source'] = {'lat': source[0].latitude, 'lng': source[0].longitude}
            context['destination'] = {'lat': destination[0].latitude, 'lng': destination[0].longitude}
        else:
            context['message'] = 'No route defined'
    except Exception as e:
        context['message'] = "Error reading route information, %s " % e
    finally:
        return JsonResponse(context)


def adddata(request):
    """
    inserts records to db reading from .xlsx file
    """
    try:
        from openpyxl import load_workbook
        wb = load_workbook(filename='path_to_data.xlsx', read_only=True)
        assert 'Sheet1' in wb
        assert 'Sheet2' in wb
    except Exception as e:
        logging.warn('library "openpyxl" should be installed & the sheet must have Sheet1 & Sheet2', e)
        return redirect('/route/')

    s1 = wb['Sheet1']
    s2 = wb['Sheet2']

    model1 = ['user_key', 'first_name', 'last_name']
    model2 = ['route_key', 'field_type', 'latitude', 'longitude']
    # for sheet 1
    users = []
    for row in s1.rows:
        r = {}
        i = 0
        for c in row:
            r[model1[i]] = c.value
            i += 1
        users.append(r)

    # for sheet 2
    routes = []
    for row in s2.rows:
        r = {}
        i = 0
        for c in row:
            r[model2[i]] = c.value
            i += 1
        routes.append(r)
    # first element is header of xlsx file, remove it
    if routes:
        routes.pop(0)
    if users:
        users.pop(0)

    for user in users:
        u = User(user_key=user['user_key'], first_name=user['first_name'],last_name=user['last_name'])
        u.save()

    for route in routes:
        r = Route(route_key=route['route_key'], field_type=route['field_type'], latitude=route['latitude'], longitude=route['longitude'])
        user = User.objects.filter(user_key=route['route_key'])
        if user:
            user = user[0]
        else:
            user = None
        r.user = user
        r.save()

    return redirect('/route/')
