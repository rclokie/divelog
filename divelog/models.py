from django.db import models
from time import gmtime, strftime
from photologue.models import Gallery

class Dive (models.Model):
    date = models.DateField()
    location = models.CharField(max_length = 250)
    gear = models.TextField(blank = True)
    weight = models.CharField(max_length=250, blank = True)
    duration = models.CharField(max_length=250, blank = True)
    temperature = models.CharField(max_length=250, blank = True)
    vis = models.CharField(max_length=250, blank = True)
    depth = models.CharField(max_length = 100, blank = True)
    comments = models.TextField(blank = True)
    mapUrl = models.CharField(blank = True, max_length=1000)
    gallery = models.ForeignKey(Gallery)
    def __unicode__(self):
        return self.date.__str__() + " - " + self.location


#class DiveGallery (models.Model):
#    dive = models.ForeignKey(Dive)
#    gallery = models.ForeignKey(Gallery)

