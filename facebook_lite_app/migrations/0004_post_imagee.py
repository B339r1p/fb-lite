# Generated by Django 3.2.4 on 2021-07-27 15:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_lite_app', '0003_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagee',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
