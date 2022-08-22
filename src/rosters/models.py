from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(
        verbose_name = "Book's name",
        max_length = 30,
    )
    description = models.TextField(
        verbose_name = "Book's description",
        blank = True,
        null = True
    )
    genre = models.ForeignKey(
        'rosters.Genre',
        on_delete=models.PROTECT,
        verbose_name="Genre",
        related_name="genres"
    )
    publishing = models.ForeignKey(
        'rosters.Publ_house',
        on_delete=models.PROTECT,
        verbose_name="Publishing",
        related_name="publishing"
    )
    author = models.ForeignKey(
        'rosters.Author',
        on_delete=models.PROTECT,
        verbose_name="Author",
        related_name="authors"
    )
    series = models.ForeignKey(
        'rosters.Series',
        on_delete=models.PROTECT,
        verbose_name="Series",
        related_name="series"
    )
    

    def __str__(self) -> str:
        return self.name


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


