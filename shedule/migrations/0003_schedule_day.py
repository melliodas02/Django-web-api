# Generated by Django 4.0.1 on 2022-01-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0002_alter_specialty_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='Day',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
