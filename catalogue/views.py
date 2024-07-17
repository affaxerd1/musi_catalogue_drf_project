from django.contrib.auth.models import User
from rest_framework import viewsets, authentication, mixins
from rest_framework import permissions
from catalogue.serializers import UserSerializer, ArtistSerializer, AlbumSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from .models import Artist, Album
from rest_framework import permissions
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView


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
        return Response({'message': 'got some data :' + str(request.data)})
    return Response({'message': 'hello world!'})


## class view
# class ArtistView(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permissions_classes = [permissions.IsAuthenticated]
#     throttle_classes = [OncePerDayUserThrottle]
#     def get(self,request):
#         artists = Artist.objects.all()
#         return Response(artists)
#
#    def post(self, request):
#         return Response({'data': request.data})

#Generic views using Generic API view
class ArtistGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#retrieve the object by id, update the object by id, delete object by id
#/artist/primarykey
class ArtistDetailGenericView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                              GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ArtistView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]


class ArtistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.AllowAny]
