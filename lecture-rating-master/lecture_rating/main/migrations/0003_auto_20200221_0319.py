# Generated by Django 2.2.4 on 2020-02-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200221_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.CharField(default='EKS3FXNF', max_length=20, primary_key=True, serialize=False),
        ),
    ]
