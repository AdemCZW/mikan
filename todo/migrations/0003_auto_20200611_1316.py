# Generated by Django 3.0 on 2020-06-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'web_member',
            },
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
    ]
