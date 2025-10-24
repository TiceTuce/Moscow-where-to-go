from django.urls import path
from . import views


urlpatterns = [
    path('<int:place_id>/', view=views.get)
]
