from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('movie_list/', movie_list, name='movie_list'),
    path('movie_detail/<int:id>/', movie_detail, name='movie_detail'),
    path('movie_create/', movie_create, name='movie_create'),
    path('movie_update/<int:id>/', movie_update, name='movie_update'),
    path('movie_delete/<int:id>/', movie_delete, name='movie_delete'),
    path('genre_list/', genre_list, name='genre_list'),
    path('genre_create/', genre_create, name='genre_create'),
    path('genre_update/<int:id>/', genre_update, name='genre_update'),
    path('genre_delete/<int:id>/', genre_delete, name='genre_delete'),
    path('comment_list/', comment_list, name='comment_list'),
    path('comment_create/<int:id>/', comment_create, name='comment_create'),
    path('comment_update/<int:id>/', comment_update, name='comment_update'),
    path('comment_delete/<int:id>/', comment_delete, name='comment_delete')
]
