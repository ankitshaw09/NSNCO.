from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Work, Artist
from .serializers import WorkSerializer

@api_view(['GET'])
def works(request):
    queryset = Work.objects.all()
    artist_name = request.query_params.get('artist', None)
    work_type = request.query_params.get('work_type', None)
    if artist_name is not None:
        artist = get_object_or_404(Artist, name=artist_name)
        queryset = artist.works.all()
    elif work_type is not None:
        queryset = queryset.filter(work_type=work_type)
    serializer = WorkSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is not None and password is not None:
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created successfully.'})
    else:
        return Response({'message': 'Please provide both username and password.'})
