# Generated by Django 3.2.5 on 2021-08-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrivalname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='items',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]