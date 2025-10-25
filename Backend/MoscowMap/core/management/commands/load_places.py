from django.core.management.base import BaseCommand
from place.models import Place, Photo
from MoscowMap.settings import MEDIA_ROOT
import requests
import wget
import os

class Command(BaseCommand):
    help = 'Displays current time'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help=u'Ссылка на JSON')

    def handle(self, *args, **kwargs):
        target_link = kwargs['link']
        
        res = requests.get(target_link)
        res_json = res.json()
        
        for place in res_json['results']:
            title = place['title']
            description_short = place['description']
            description_long = place['body_text'],
            lng = place['coords']['lon']
            lat = place['coords']['lat']
            
            if not all((title, description_short, description_long, lng, lat)):
                continue
            
            new_place = Place.objects.create(
                title=title,
                description_short=description_short,
                description_long=description_long,
                lng=lng,
                lat=lat
            )
            print(f'\nМесто "{new_place.title}" успешно создано')
            
            for index, image_info in enumerate(place['images'][:10]):
                image_url = image_info['image']
                downloaded_img_path = wget.download(image_url, os.path.join(MEDIA_ROOT, 'places'))
                Photo.objects.create(
                    place=new_place,
                    image=downloaded_img_path,
                    position=index
                )
                