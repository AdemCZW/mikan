# Generated by Django 3.2.5 on 2021-11-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shotdogs_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo_1001', models.CharField(blank=True, max_length=1000, verbose_name='-狗狗-')),
                ('Photo_1002', models.CharField(blank=True, max_length=1000, verbose_name='2')),
                ('Photo_1003', models.CharField(blank=True, max_length=1000, verbose_name='3')),
                ('Photo_1004', models.CharField(blank=True, max_length=1000, verbose_name='4')),
                ('Photo_1005', models.CharField(blank=True, max_length=1000, verbose_name='5')),
                ('Photo_1006', models.CharField(blank=True, max_length=1000, verbose_name='6')),
                ('Photo_1007', models.CharField(blank=True, max_length=1000, verbose_name='7')),
                ('Photo_1008', models.CharField(blank=True, max_length=1000, verbose_name='8')),
                ('Photo_1009', models.CharField(blank=True, max_length=1000, verbose_name='9')),
                ('Photo_1010', models.CharField(blank=True, max_length=1000, verbose_name='10')),
                ('Photo_2001', models.CharField(blank=True, max_length=1000, verbose_name='-貓咪-')),
                ('Photo_2002', models.CharField(blank=True, max_length=1000, verbose_name='2')),
                ('Photo_2003', models.CharField(blank=True, max_length=1000, verbose_name='3')),
                ('Photo_2004', models.CharField(blank=True, max_length=1000, verbose_name='4')),
                ('Photo_2005', models.CharField(blank=True, max_length=1000, verbose_name='5')),
                ('Photo_2006', models.CharField(blank=True, max_length=1000, verbose_name='6')),
                ('Photo_2007', models.CharField(blank=True, max_length=1000, verbose_name='7')),
                ('Photo_2008', models.CharField(blank=True, max_length=1000, verbose_name='8')),
                ('Photo_2009', models.CharField(blank=True, max_length=1000, verbose_name='9')),
                ('Photo_2010', models.CharField(blank=True, max_length=1000, verbose_name='10')),
                ('Photo_3001', models.CharField(blank=True, max_length=1000, verbose_name='-婚紗-')),
                ('Photo_3002', models.CharField(blank=True, max_length=1000, verbose_name='2')),
                ('Photo_3003', models.CharField(blank=True, max_length=1000, verbose_name='3')),
                ('Photo_3004', models.CharField(blank=True, max_length=1000, verbose_name='4')),
                ('Photo_3005', models.CharField(blank=True, max_length=1000, verbose_name='5')),
                ('Photo_3006', models.CharField(blank=True, max_length=1000, verbose_name='6')),
                ('Photo_3007', models.CharField(blank=True, max_length=1000, verbose_name='7')),
                ('Photo_3008', models.CharField(blank=True, max_length=1000, verbose_name='8')),
                ('Photo_3009', models.CharField(blank=True, max_length=1000, verbose_name='9')),
                ('Photo_3010', models.CharField(blank=True, max_length=1000, verbose_name='10')),
                ('Photo_4001', models.CharField(blank=True, max_length=1000, verbose_name='-其他-')),
                ('Photo_4002', models.CharField(blank=True, max_length=1000, verbose_name='2')),
                ('Photo_4003', models.CharField(blank=True, max_length=1000, verbose_name='3')),
                ('Photo_4004', models.CharField(blank=True, max_length=1000, verbose_name='4')),
                ('Photo_4005', models.CharField(blank=True, max_length=1000, verbose_name='5')),
                ('Photo_4006', models.CharField(blank=True, max_length=1000, verbose_name='6')),
                ('Photo_4007', models.CharField(blank=True, max_length=1000, verbose_name='7')),
                ('Photo_4008', models.CharField(blank=True, max_length=1000, verbose_name='8')),
                ('Photo_4009', models.CharField(blank=True, max_length=1000, verbose_name='9')),
                ('Photo_4010', models.CharField(blank=True, max_length=1000, verbose_name='10')),
            ],
            options={
                'verbose_name': '寵物寫真',
                'verbose_name_plural': '寵物寫真',
            },
        ),
    ]