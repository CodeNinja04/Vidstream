# Generated by Django 3.2b1 on 2021-03-17 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0011_movieproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieproxy',
            options={'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
    ]