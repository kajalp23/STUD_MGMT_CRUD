# Generated by Django 3.1.7 on 2021-05-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210523_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
