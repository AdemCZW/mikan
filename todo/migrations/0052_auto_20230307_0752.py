# Generated by Django 3.2.5 on 2023-03-07 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0051_wedding_form_001'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding_form_001',
            name='wed_001_address',
            field=models.CharField(default='', max_length=1000, verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='wedding_form_001',
            name='wed_001_email',
            field=models.CharField(default='', max_length=1000, verbose_name='信箱'),
        ),
        migrations.AddField(
            model_name='wedding_form_001',
            name='wed_001_items_01',
            field=models.CharField(default='', max_length=1000, verbose_name='產品項目'),
        ),
        migrations.AddField(
            model_name='wedding_form_001',
            name='wed_001_items_02',
            field=models.CharField(default='', max_length=1000, verbose_name='預約套系'),
        ),
        migrations.AddField(
            model_name='wedding_form_001',
            name='wed_001_items_03',
            field=models.CharField(default='', max_length=1000, verbose_name='娘家冊/掌中本'),
        ),
        migrations.AddField(
            model_name='wedding_form_001',
            name='wed_001_items_04',
            field=models.CharField(default='', max_length=1000, verbose_name='放大商品'),
        ),
        migrations.AddField(
            model_name='wedding_form_001',
            name='wed_001_phone_m',
            field=models.CharField(default='', max_length=1000, verbose_name='新郎電話'),
        ),
        migrations.AddField(
            model_name='wedding_form_001',
            name='wed_001_phone_w',
            field=models.CharField(default='', max_length=1000, verbose_name='新娘電話'),
        ),
        migrations.AlterField(
            model_name='wedding_form_001',
            name='wed_001_name_w',
            field=models.CharField(default='', max_length=1000, verbose_name='新娘姓名'),
        ),
    ]
