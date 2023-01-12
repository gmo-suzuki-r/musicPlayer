# Generated by Django 4.1.5 on 2023-01-11 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicPlayerApp', '0005_alter_album_album_jacket_alter_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='audio_file',
            field=models.FileField(null=True, upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_jacket',
            field=models.ImageField(upload_to='img'),
        ),
    ]
