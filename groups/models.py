from django.db import models


class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    pet = models.ForeignKey(
        "pets.Pet",
        on_delete=models.CASCADE,
        related_name="groups",
    )

    def __repr__(self) -> str:
        return f"<Pet [{self.id}] - {self.scientific_name}"


# N para 1 com pet
