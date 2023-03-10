from django.db import models


class Trait(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"<Pet [{self.id}] - {self.name}"
