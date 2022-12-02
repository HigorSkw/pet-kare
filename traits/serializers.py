from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from traits.models import Trait


class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    created_at = serializers.DateField(read_only=True)
