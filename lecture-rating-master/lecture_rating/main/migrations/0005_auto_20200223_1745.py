# Generated by Django 2.2.3 on 2020-02-23 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_merge_20200223_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='not_reco',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lecture',
            name='reco',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lectureratingboard',
            name='homework',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lectureratingboard',
            name='pro_lecturePower',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lectureratingboard',
            name='project',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lectureratingboard',
            name='semester',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='lectureratingboard',
            name='semester_year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lectureratingboard',
            name='test_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.CharField(default='92E5GC0T', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('student_number', models.CharField(max_length=20)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.University')),
            ],
        ),
    ]
