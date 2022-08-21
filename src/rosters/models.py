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

    def __str__(self) -> str:
        return self.name



class Genre(models.Model):
    book = models.ForeignKey(
        'rosters.Book',
        on_delete = models.PROTECT,
        verbose_name="Book",
        related_name="genres"
    )
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
    book = models.ForeignKey(
        'rosters.Book',
        on_delete = models.PROTECT,
        verbose_name="Book",
        related_name="authors"
    )
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
    book = models.ForeignKey(
        'rosters.Book',
        on_delete = models.PROTECT,
        verbose_name="Book",
        related_name="series"
    )
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
    book = models.ForeignKey(
        'rosters.Book',
        on_delete = models.PROTECT,
        verbose_name="Book",
        related_name="publs"
    )
    name = models.CharField(
        verbose_name = "Publ_house name",
        max_length = 30,
    )

    def __str__(self) -> str:
        return self.name