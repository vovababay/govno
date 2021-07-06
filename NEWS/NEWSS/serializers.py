from rest_framework import serializers
from NEWSS.models import NEWSS, Themes
from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter


class ThemeSerializer(serializers.ModelSerializer):





    class Meta:
        model = Themes
        fields = ('title',)


   

class NewsSerializer(serializers.ModelSerializer):

    class Meta:

        model = NEWSS
        fields = (
            "name",
            'description',
            'date_of_creation',
            'date_of_update',
            'status',
            'theme',
            'image',
        )