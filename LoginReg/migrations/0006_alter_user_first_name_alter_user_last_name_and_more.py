# Generated by Django 4.1.4 on 2023-04-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginReg', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='First_name',
            field=models.CharField(help_text='Enter your First name', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='Last_name',
            field=models.CharField(help_text='Enter your Last name', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Enter your Username', max_length=20, unique=True),
        ),
    ]
