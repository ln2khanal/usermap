from django.contrib import admin
from route.models import User, Route


class UserAdmin(admin.ModelAdmin):
    empty_value_display = 'N/A'
    list_display = ('first_name', 'last_name', 'user_key')
    search_fields = ('first_name', 'last_name')


class RouteAdmin(admin.ModelAdmin):
    empty_value_display = 'N/A'
    list_display = ('user', 'route_key', 'latitude', 'longitude', 'field_type')
    search_fields = ('user', 'route_key', 'latitude', 'longitude')

admin.site.register(User, UserAdmin)
admin.site.register(Route, RouteAdmin)
