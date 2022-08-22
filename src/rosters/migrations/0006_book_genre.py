# Generated by Django 4.0.6 on 2022-08-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0005_publ_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='genres', to='rosters.genre', verbose_name='Genre'),
        ),
    ]