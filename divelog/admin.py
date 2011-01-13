from divelog.models import Dive
from divelog.models import Photo
from django.contrib import admin

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 2

class DiveAdmin(admin.ModelAdmin):
    fields = ['date','location','duration','vis','temperature','depth','gear','weight','comments','mapUrl']
    inlines = [PhotoInline]

admin.site.register(Dive,DiveAdmin)

