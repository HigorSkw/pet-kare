from rest_framework import serializers
from groups.models import Group
from rest_framework.validators import UniqueValidator


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    scientific_name = serializers.CharField(
        max_length=50,
        validators=[
            UniqueValidator(
                queryset=Group.objects.all(),
                message="Scientific name is already exists!",
            ),
        ],
    )
    created_at = serializers.DateField(read_only=True)

    # Forma "Manual"

    # def validate_email(self, scientific_name: str) -> str:

    #     scientific_name_exists = Group.objects.filter(
    #         scientific_name=scientific_name
    #     ).exists()

    #     if scientific_name_exists:
    #         raise serializers.ValidationError(
    #             detail="Scientific name is already exists!"
    #         )

    #     return scientific_name
