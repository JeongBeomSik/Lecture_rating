# Generated by Django 2.2.4 on 2020-02-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200221_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.CharField(default='HNXYDTHC', max_length=20, primary_key=True, serialize=False),
        ),
    ]
