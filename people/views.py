from rest_framework import generics, viewsets, mixins
from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from people.models import People, Category
from people.serializers import PeopleSerializer


class PeopleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @action(methods=['get'], detail=False)
    def category(self, request):
        categories = Category.objects.all()
        return Response({'categories': [c.name for c in categories]})


# class PeopleAPIList(generics.ListCreateAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
#
#
# class PeopleAPIUpdate(generics.UpdateAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
#
#
# class PeopleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer


