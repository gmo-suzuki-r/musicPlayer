# Generated by Django 4.1.5 on 2023-01-11 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicPlayerApp', '0007_alter_album_album_jacket_alter_album_audio_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='song_lyric',
            field=models.TextField(blank=True, null=True),
        ),
    ]
