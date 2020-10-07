from rest_framework import serializers
from .models import Competition


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = "__all__"
        lookup_field = 'slug'

