from django.db import models

from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    country = models.CharField(
        max_length=100
    )

    def __str__(self):
        return (f""
                f"{self.name} "
                f"({self.country})")

    class Meta:
        ordering = ("name", )


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=100,
        unique=True
    )

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return (f""
                f"{self.username}: "
                f"{self.first_name} "
                f"{self.last_name}")


class Car(models.Model):
    model = models.CharField(
        max_length=100
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars")

    class Meta:
        ordering = ("model", )

    def __str__(self):
        return (f""
                f"{self.model} "
                f"({self.manufacturer.name})")
