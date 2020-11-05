from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import HttpResponse

from media_retriever.models import Media

@api_view(['POST'],)
#@permission_classes((IsAuthenticated, ))
def getAll(request):
    IDs = request.POST.get('IDs', None)
    types = request.POST.get('types', None)
    names = request.POST.get('names', None)
    
    medias = None
    try:
        if IDs:
            medias = Media.objects.filter(id__in=IDs).values()
        elif types:
            medias = Media.objects.filter(type__in=types).values()
        elif names:
            medias = Media.objects.filter(names__in=names).values()
    except Exception as e:
        print(str(e))
        return Response({ 'status': '1', 'error': str(e) })


    return Response({ 'status': '0', 'data': medias})

