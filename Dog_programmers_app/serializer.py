from rest_framework import serializers
from .models import Dog, ProgrammingLanguage


class DogSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Dog
        fields = {'id','name'}


class ProgrammingLanguageSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = {'id', 'languages_names'}


