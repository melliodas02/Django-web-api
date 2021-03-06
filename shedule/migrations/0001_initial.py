# Generated by Django 4.0.1 on 2022-01-13 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=255)),
                ('Number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, unique=True)),
                ('Building', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.IntegerField(max_length=2)),
                ('Group', models.CharField(max_length=255)),
                ('SubGroup', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=255)),
                ('ScientificDegree', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='shedule.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, unique=True)),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialty', to='shedule.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectNumber', models.IntegerField(max_length=16)),
                ('SubjectStartTime', models.TimeField()),
                ('SubjectEndTime', models.TimeField()),
                ('Semester', models.IntegerField()),
                ('ClassRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='shedule.classroom')),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='shedule.group')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='shedule.subject')),
                ('SubjectType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='shedule.subjecttype')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='Specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Group', to='shedule.specialty'),
        ),
    ]
