from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(
        verbose_name = "Genre name",
        max_length = 30,
    )
    description = models.TextField(
        verbose_name = "Genre description",
        blank = True,
        null = True
    )

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(
        verbose_name = "Author's name",
        max_length = 30,
    )
    description = models.TextField(
        verbose_name = "Author's description",
        blank = True,
        null = True
    )

    def __str__(self) -> str:
        return self.name



class Series(models.Model):
    name = models.CharField(
        verbose_name = "Series name",
        max_length = 30,
    )
    description = models.TextField(
        verbose_name = "Series description",
        blank = True,
        null = True
    )

    def __str__(self) -> str:
        return self.name


class Publ_house(models.Model):
    name = models.CharField(
        verbose_name = "Publ_house name",
        max_length = 30,
    )

    def __str__(self) -> str:
        return self.name