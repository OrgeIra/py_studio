from django.urls import path

from main import views

app_name='maim'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name='about'),

]