from django.urls import path
from .views import Goodbye
urlpatterns = [
    path('', Goodbye, name='Goodbye')]