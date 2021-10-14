# Generated by Django 3.2.7 on 2021-09-29 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_rename_name_video_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Published Video',
                'verbose_name_plural': 'Published Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]
