# Generated by Django 3.2.5 on 2021-07-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_flight_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='items',
            field=models.CharField(default=' ', max_length=10),
        ),
    ]
