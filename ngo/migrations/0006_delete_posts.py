# Generated by Django 4.1.4 on 2023-04-08 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0005_posts_ngo_name_posts_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
