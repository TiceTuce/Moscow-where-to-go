from django.shortcuts import render
from django.core import serializers

from place.models import Place

# Create your views here.
def home(request):
    
    places = serializers.serialize('python', Place.objects.all())
    
    features = []
    for place in places:
        place_id = place['pk']
        place_fields = place['fields']
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place_fields['lng'], place_fields['lat']]
            },
            'properties': {
                'title': place_fields['title'],
                'placeId': place_id,
                'detailsUrl': f'http://127.0.0.1:8000/places/{place_id}'
            }
        }
        features.append(feature)
        
    output_data = {'geoJson': {
        'type': 'FeatureCollection',
        'features': features 
    }}
    
    return render(request, './map/index.html', context=output_data)
