from rest_framework import serializers
from pets.models import SexPet, Pet
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from groups.models import Group
from traits.models import Trait


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexPet.choices,
        default=SexPet.NOT_INFORMED,
    )

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    traits_count = serializers.SerializerMethodField()

    # Estudar os serialiazer.methodfield

    def get_traits_count(self, obj):

        count = 0

        for number in obj.traits.all():

            count = count + 1

        return count

    def create(self, validated_data: dict) -> Pet:

        group_data = validated_data.pop("group")
        trait_data = validated_data.pop("traits")

        group_obj = Group.objects.get_or_create(**group_data)[0]

        newPet = Pet.objects.create(**validated_data, group=group_obj)

        for trait in trait_data:
            trait_obj = Trait.objects.get_or_create(**trait)[0]
            newPet.traits.add(trait_obj)

        return newPet

    def update(self, istance, validated_data: dict) -> Pet:
        group_data: dict = validated_data.pop("group", None)
        trait_data = validated_data.pop("traits", None)

        if group_data is not None:
            group_obj, created = Group.objects.get_or_create(pets=istance)
            for key, value in group_data.items():
                setattr(group_obj, key, value)
            group_obj.save()

        if trait_data is not None:
            list = []
            for trait in trait_data:
                trait_obj = Trait.objects.get_or_create(**trait)[0]
                list.append(trait_obj)
            istance.traits.set(list)

        for key, value in validated_data.items():
            setattr(istance, key, value)

        istance.save()

        return istance
