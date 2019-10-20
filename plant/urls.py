from django.urls import path
from .views import PlantListView, PlantDetailView, PlantUpdateView
from . import views

urlpatterns = [
	path('new/', views.PlantCreateView, name='plant-create'),
	path('all/', PlantListView.as_view(), name='plant-list'),
	path('<uuid:pk>/', PlantDetailView.as_view(), name='plant-detail'),
	path('<uuid:pk>/update/', PlantUpdateView.as_view(), name='plant-update'),
]