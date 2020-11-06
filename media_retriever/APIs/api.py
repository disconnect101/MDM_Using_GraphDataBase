from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import HttpResponse
from django.conf import settings
import os
from media_retriever import utils

from media_retriever.models import Media

@api_view(['POST'],)
#@permission_classes((IsAuthenticated, ))
def getAll(request):
    #print(request.POST)
    IDs = request.POST.getlist('IDs[]', None)
    types = request.POST.getlist('types[]', None)
    names = request.POST.getlist('names[]', None)
    print(IDs)

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

    for media in medias:
        if media.get('type') == 'CSV':
            path = os.path.join(settings.BASE_DIR, 'media/'+media.get('media'))
            fields, rows = utils.csv_reader(path)
            media.update({ 'fields': fields, 'rows': rows})
    return Response({ 'status': '0', 'data': medias})


@api_view(['POST'],)
#@permission_classes((IsAuthenticated, ))
def get(request):
    #print(request.POST)
    ID = request.POST.get('ID', None)

    media = None
    try:
        if ID:
            media = Media.objects.filter(id=ID)
            if media.count() > 0:
                media = media.values()[0]
            else:
                return Response({ 'status': '1', 'error': 'No such ID exists' })
    except Exception as e:
        print(str(e))
        return Response({ 'status': '1', 'error': str(e) })

    if media.get('type') == 'CSV':
        path = os.path.join(settings.BASE_DIR, 'media/' + media.get('media'))
        fields, rows = utils.csv_reader(path)
        media.update({'fields': fields, 'rows': rows})

    return Response({ 'status': '0', 'data': media})


