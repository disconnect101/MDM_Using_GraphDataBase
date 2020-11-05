from django.urls import path, include
from media_retriever.APIs import api


urlpatterns = [
    path('getAll/', api.getAll),
]