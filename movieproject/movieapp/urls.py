from . import views
from django.contrib import admin
from django.urls import path, include
app_name = 'movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>',views.details,name='details'),
    path('add/',views.add_movie,name='add_movie'),
    path('delete/<int:id>',views.delete,name='delete')
]
