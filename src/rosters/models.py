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