# Generated by Django 2.2.4 on 2020-02-24 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0004_auto_20200224_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectureratingboard',
            name='lecture',
        ),
        migrations.RemoveField(
            model_name='lectureratingboard',
            name='user',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='university',
        ),
        migrations.RemoveField(
            model_name='user',
            name='university',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
        migrations.DeleteModel(
            name='LectureRatingBoard',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.DeleteModel(
            name='University',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
