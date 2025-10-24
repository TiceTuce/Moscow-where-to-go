from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=120)
    description_short = models.TextField(max_length=500)
    description_long = models.TextField(max_length=1500)
    lng = models.FloatField()
    lat = models.FloatField()
    

class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="places")
    