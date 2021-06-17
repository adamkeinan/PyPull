from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Pilot
from .serializers import PilotSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.request import Request
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PilotList(APIView):
    """
    List all pilot, or create a new pilot.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        pilot = Pilot.objects.all()
        serializer = PilotSerializer(pilot, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PilotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PilotDetail(APIView):
    """
    Retrieve, update or delete a pilot instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Pilot.objects.get(pk=pk)
        except Pilot.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pilot = self.get_object(pk)
        serializer = PilotSerializer(pilot)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pilot = self.get_object(pk)
        serializer = PilotSerializer(pilot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pilot = self.get_object(pk)
        pilot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PilotDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
class PilotList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
