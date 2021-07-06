from django.shortcuts import render
from NEWSS.models import NEWSS, Themes
from rest_framework import  viewsets,permissions
from .serializers import NewsSerializer,ThemeSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NEWSS.objects.all()
    permissions_clases = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer



class ThemeViewSet(viewsets.ModelViewSet):

    queryset = Themes.objects.all()
    permissions_clases = [
        permissions.AllowAny
    ]
    serializer_class = ThemeSerializer


