from divelog.models import Dive
#from divelog.models import DiveGallery
from django.contrib import admin
from photologue.admin import GalleryAdmin

#class PhotoInline(admin.TabularInline):
#    model = Photo
#    extra = 2

class DiveAdmin(admin.ModelAdmin):
    fields = ['date','location','duration','vis','temperature','depth','gear','weight','comments','mapUrl','gallery']
#    inlines = [PhotoInline]

#class DiveGalleryAdmin(admin.ModelAdmin):
#    def __unicode__(self):
#        return dive
#    fields = ['dive','gallery']

admin.site.register(Dive,DiveAdmin)
#admin.site.register(DiveGallery, DiveGalleryAdmin)

