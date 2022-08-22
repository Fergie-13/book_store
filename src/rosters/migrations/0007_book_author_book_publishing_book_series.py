# Generated by Django 4.0.6 on 2022-08-21 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0006_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='authors', to='rosters.author', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='publishing', to='rosters.publ_house', verbose_name='Publishing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='series', to='rosters.series', verbose_name='Series'),
            preserve_default=False,
        ),
    ]
