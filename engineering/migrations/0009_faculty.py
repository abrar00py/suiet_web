# Generated by Django 4.0.3 on 2022-11-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineering', '0008_alter_events_discription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='static/img/Engineeringimage/Faculty')),
                ('qualification', models.TextField()),
                ('description', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=50)),
                ('Teaching_Experience', models.IntegerField()),
                ('Industry_Experience', models.IntegerField()),
                ('Research_Experience', models.IntegerField()),
            ],
        ),
    ]
