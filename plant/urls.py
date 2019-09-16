from django.urls import path
from .views import PlantListView
from . import views

urlpatterns = [
	path('new/', views.plant, name='plant-create'),
	path('all/', PlantListView.as_view(), name='plant-list'),
]