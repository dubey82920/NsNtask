from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from NsN.models import Work,Artist
from .serializers import WorkSerializer,ArtistSerializer


@api_view(['GET'])
def getRoutes(request):

    routes=[
       

        {'GET':'/api/work'},
        {'GET':'/api/work/<str:artist_name>'},
        {'GET':'/api/work/<str:work_type>'},
        {'GET':'api/register'},
    ]
    return Response(routes)
@api_view(['GET'])
def getWorks(request):
    work=Work.objects.all()
    serializer=WorkSerializer(work,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWork(request,artist_name):
    work=Artist.objects.get(name=artist_name)
    serializer=ArtistSerializer(work,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getWorkType(request,work_type):
    work=Work.objects.get(work_type=work_type)
    serializer=WorkSerializer(work,many=False)
    return Response(serializer.data)



@api_view(['POST'])
def register(request):
     username = request.data.get('username')
     password = request.data.get('password')
     if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)
     else:
         return Response({'success':'successfuly created'}, status=status.HTTP_200_OK)

