from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict
from .models import Pet
from .serializers import PetSerializer
from django.shortcuts import get_object_or_404


class PetView(APIView):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()

        serializer = PetSerializer(pets, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        pet = Pet.objects.create(**serializer.validated_data)

        serializer = PetSerializer(pet)

        return Response(serializer.data, status.HTTP_201_CREATED)


class PetDetailView(APIView):
    def get(self, request: Request, pet_id: int) -> Response:
        try:
            pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response({"detail": "pet not found"}, status.HTTP_404_NOT_FOUND)

        serializer = PetSerializer(pet)
        return Response(serializer.data)

    def patch(self, request: Request, pet_id: int) -> Response:

        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)

        return Response(serializer.data)

    def delete(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
