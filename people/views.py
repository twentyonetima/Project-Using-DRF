from rest_framework import generics
from django.shortcuts import render

# Create your views here.
from people.models import People
from people.serializers import PeopleSerializer


class PeopleAPIView(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
