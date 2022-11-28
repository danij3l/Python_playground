from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addAnimal),
    path('updateOrDelete/<int:pk>', views.AnimalDetail.as_view()),
]
