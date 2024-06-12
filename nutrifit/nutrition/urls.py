from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_recipes, name='recipesearch'),
    path('recipe/<int:recipe_id>/', views.recipe_details, name='details'),
    path('delete_grafica/<int:recipe_id>/', views.delete_grafica, name='delete_grafica'),
]
