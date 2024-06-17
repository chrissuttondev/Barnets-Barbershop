from django.urls import path
from . import views as gallery_views

urlpatterns = [
    path('', gallery_views.gallery, name='gallery'),

]
