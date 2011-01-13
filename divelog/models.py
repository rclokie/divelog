from django.db import models
from time import gmtime, strftime

# TODO move this somewhere
class PhotoPath:
    def __call__(self, instance, filename):
        return strftime("%Y-%m-%d/",gmtime()) + filename

# Create your models here.
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

    def __unicode__(self):
        return self.date.__str__() + " - " + self.location


class Photo (models.Model):
    dive = models.ForeignKey(Dive)
    image = models.ImageField(upload_to=PhotoPath()) 
    caption = models.TextField(blank = True)

    def __unicode__(self):
        if (self.image == None ):
            return "No Image"
        return self.image.name + " (dive " + self.dive.__unicode__() + ")"

