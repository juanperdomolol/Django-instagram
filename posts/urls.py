"""posts url """
# Django
from django.urls import path
#django

from posts import views

urlpatterns = [
    path(
        route='',
        view= views.list_posts,
        name='feed'),
    path(
        route='posts/new',
        view= views.create_post,
        name ='create'),
]