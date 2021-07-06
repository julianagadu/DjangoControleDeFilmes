from django.contrib import admin
from django.urls import path
from . import views
#from .views import HomePageView, CreatePostView

urlpatterns = [
    path('home/', views.Homeview, name='home'),
    path('home/novo', views.CreateFilme, name='novo'),
    path('home/detail/<int:id>', views.FilmeDetail, name='detail'),
    path('home/detail/<int:id>/editar', views.UpdateFilme, name='editar'),
    path('home/detail/<int:id>/delete', views.DeleteFilme, name='delete')
]   