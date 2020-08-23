from django.contrib import admin
from .models import Film
from .models import Person
from .models import LastUpdated

class FilmAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['heroku_id', 'title']}),
    ]
    list_display = ('heroku_id', 'title')
    list_filter = ['title']


admin.site.register(Film)


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['heroku_id', 'name']}),
        (None, {'fields': ['films']}),
    ]
    list_display = ('heroku_id', 'name', 'films')
    list_filter = ['name']


admin.site.register(Person)


class LastUpdatedAdmin(admin.ModelAdmin):
    fieldsets = [
        ('timefield',               {'fields': ['time']}),
    ]
    list_display = ('time')
    list_filter = ['time']


admin.site.register(LastUpdated)