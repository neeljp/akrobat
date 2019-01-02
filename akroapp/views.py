#from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User
from akroapp.models import Exercise,Tag
from akroapp.serializers import ExerciseSerializer,UserSerializer,TagSerializer
from rest_framework import generics,permissions, renderers, viewsets
from akroapp.permissions import IsCreaterOrReadOnly
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This vieswets provides list and detail actions..
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    '''
    List, create ,retrieve, update and destroy actions
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsCreaterOrReadOnly)
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def perform_create(self, serializer):
        serializer.save(creater=self.request.user)
        
class TagViewSet(viewsets.ModelViewSet):
    '''
    List, create ,retrieve, update and destroy actions
    '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

