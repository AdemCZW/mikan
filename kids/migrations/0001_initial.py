# Generated by Django 3.2.5 on 2022-05-26 12:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kid_index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kid_home_001', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動種類-1')),
                ('kid_home_002', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動標題-1')),
                ('kid_home_003', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動日期-1')),
                ('kid_home_004', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動連結-1')),
                ('kid_home_005', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動種類-2')),
                ('kid_home_006', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動標題-2')),
                ('kid_home_007', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動日期-2')),
                ('kid_home_008', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動連結-2')),
                ('kid_home_009', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動種類-3')),
                ('kid_home_010', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動標題-3')),
                ('kid_home_011', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動日期-3')),
                ('kid_home_012', models.CharField(blank=True, default='', max_length=1000, verbose_name='活動連結-3')),
                ('kid_service_001', models.CharField(blank=True, default='', max_length=1000, verbose_name='服務標題-1')),
                ('kid_service_002', models.CharField(blank=True, default='', max_length=1000, verbose_name='服務內容-1')),
                ('kid_service_003', models.CharField(blank=True, default='', max_length=1000, verbose_name='服務標題-2')),
                ('kid_service_004', models.CharField(blank=True, default='', max_length=1000, verbose_name='服務內容-2')),
                ('kid_service_005', models.CharField(blank=True, default='', max_length=1000, verbose_name='服務標題-3')),
                ('kid_service_006', models.CharField(blank=True, default='', max_length=1000, verbose_name='服務內容-3')),
                ('kid_service_007', models.CharField(blank=True, default='', max_length=1000, verbose_name='服務標題-4')),
                ('kid_service_008', models.CharField(blank=True, default='', max_length=1000, verbose_name='服務內容-4')),
                ('kid_photos_001', models.CharField(blank=True, default='', max_length=1000, verbose_name='情境')),
                ('kid_photos_002', models.CharField(blank=True, default='', max_length=1000, verbose_name='抓周')),
                ('kid_photos_003', models.CharField(blank=True, default='', max_length=1000, verbose_name='道具')),
                ('kid_photos_004', models.CharField(blank=True, default='', max_length=1000, verbose_name='新生兒')),
                ('kid_plans_001', models.CharField(blank=True, default='', max_length=1000, verbose_name='Ａ方案-原價')),
                ('kid_plans_002', models.CharField(blank=True, default='', max_length=1000, verbose_name='Ａ方案-特價')),
                ('kid_plans_003', ckeditor.fields.RichTextField(blank=True, default='輸入', max_length=2000, null=True, verbose_name='Ａ方案-內容')),
                ('kid_plans_004', models.CharField(blank=True, default='', max_length=1000, verbose_name='Ｂ方案-原價')),
                ('kid_plans_005', models.CharField(blank=True, default='', max_length=1000, verbose_name='Ｂ方案-特價')),
                ('kid_plans_006', ckeditor.fields.RichTextField(blank=True, default='輸入', max_length=2000, null=True, verbose_name='Ｂ方案-內容')),
                ('kid_plans_007', models.CharField(blank=True, default='', max_length=1000, verbose_name='Ｃ方案-原價')),
                ('kid_plans_008', models.CharField(blank=True, default='', max_length=1000, verbose_name='Ｃ方案-特價')),
                ('kid_plans_009', ckeditor.fields.RichTextField(blank=True, default='輸入', max_length=2000, null=True, verbose_name='Ｃ方案-內容')),
                ('kid_phone_001', models.CharField(blank=True, default='', max_length=1000, verbose_name='電話')),
                ('kid_mail_001', models.CharField(blank=True, default='', max_length=1000, verbose_name='信箱')),
                ('kid_line_001', models.CharField(blank=True, default='', max_length=1000, verbose_name='line')),
                ('kid_fb_001', models.CharField(blank=True, default='', max_length=1000, verbose_name='facebook')),
                ('kid_ig_001', models.CharField(blank=True, default='', max_length=1000, verbose_name='instagram')),
            ],
            options={
                'verbose_name': '兒童抓周網站',
                'verbose_name_plural': '兒童抓周網站',
            },
        ),
    ]
