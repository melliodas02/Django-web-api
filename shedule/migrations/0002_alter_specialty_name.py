# Generated by Django 4.0.1 on 2022-01-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='Name',
            field=models.CharField(max_length=255),
        ),
    ]
