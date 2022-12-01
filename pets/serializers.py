from rest_framework import serializers
from pets.models import SexPet
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexPet.choices,
        default=SexPet.NOT_INFORMED,
    )

    group = GroupSerializer(read_only=True)
    traits = TraitSerializer(read_only=True, many=True)
