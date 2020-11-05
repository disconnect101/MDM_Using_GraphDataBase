from django.urls import path, include

urlpatterns = [
    path('api/', include('media_retriever.APIs.urls')),
]