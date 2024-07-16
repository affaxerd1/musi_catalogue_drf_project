from django.contrib.auth.models import User
from rest_framework import viewsets, authentication
from rest_framework import permissions
from catalogue.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import  APIView
from .models import Artist
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be views or edited
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'
@api_view(['GET', 'POST'])
@throttle_classes([OncePerDayUserThrottle])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message' : 'got some data :' + str(request.data)} )
    return Response({'message':'hello world!'})

class ArtistView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]
    throttle_classes = [OncePerDayUserThrottle]
    def get(self,request):
        artists = Artist.objects.all()
        return Response(artists)
    def post(self, request):
        return Response({'data': request.data})