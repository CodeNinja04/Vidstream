# Generated by Django 3.1.12 on 2021-10-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.IntegerField(blank=True, choices=[(None, 'Rate this'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], null=True),
        ),
    ]
