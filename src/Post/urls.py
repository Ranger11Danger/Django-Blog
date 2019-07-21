from django.urls import path
from .views import home, projects

urlpatterns = [
    path('', home),
    path('projects', projects),
]