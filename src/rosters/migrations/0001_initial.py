# Generated by Django 4.0.6 on 2022-08-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name="Book's name")),
                ('description', models.TextField(blank=True, null=True, verbose_name="Book's description")),
            ],
        ),
    ]
