# Generated by Django 4.1.3 on 2023-04-06 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='desciption',
            new_name='description',
        ),
    ]
