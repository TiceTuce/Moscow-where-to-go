from django.http import JsonResponse
from django.conf import settings

from .models import Place, Photo

# Create your views here.

def get(request, place_id):
    place = Place.objects.get(pk=place_id)
    imgs = Photo.objects.filter(place=place_id)
    output_data = {
        'title': place.title,
        'imgs': [settings.MEDIA_URL+str(img.image) for img in imgs],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    
    return JsonResponse(output_data)
