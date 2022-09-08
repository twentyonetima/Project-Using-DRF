from rest_framework import generics, viewsets, mixins
from django.shortcuts import render


# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from people.models import People, Category
from people.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from people.serializers import PeopleSerializer


class PeopleAPIList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PeopleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class PeopleAPIDetailView(generics.RetrieveDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAdminOrReadOnly, )


