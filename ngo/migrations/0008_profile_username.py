# Generated by Django 4.0.4 on 2023-04-09 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0007_alter_feedback_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
