from django.db import models

class Place(models.Model):
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
    
    title = models.CharField(
        max_length=120, 
        verbose_name='Название'
    )
    description_short = models.TextField(
        max_length=500,
        verbose_name='Короткое описание'    
    )
    description_long = models.TextField(
        max_length=1500,
        verbose_name='Полное описание'
    )
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    
    def __str__(self):
        return self.title
    

class Photo(models.Model):
    class Meta:
        ordering = ["position"]
    
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField(upload_to="places", verbose_name='Картинка')
    position = models.IntegerField(default=1, verbose_name='Позиция')
    
    def __str__(self):
        return self.image.url
    