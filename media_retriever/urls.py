from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', home),
    path('api/', include('media_retriever.APIs.urls')),
]