# Generated by Django 4.0.3 on 2022-11-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.IntegerField(),
        ),
    ]
