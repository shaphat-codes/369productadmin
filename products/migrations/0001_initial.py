# Generated by Django 4.0 on 2023-03-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(default='', max_length=300)),
                ('category_id', models.CharField(max_length=1000)),
                ('brand_id', models.CharField(default='', max_length=1000)),
                ('video_provider', models.CharField(default='youtube', max_length=1000)),
                ('video_link', models.CharField(default='', max_length=1000)),
                ('tags', models.CharField(max_length=1000)),
                ('unit_price', models.CharField(max_length=1000)),
                ('purchase_price', models.CharField(max_length=1000)),
                ('unit', models.CharField(max_length=1000)),
                ('slug', models.CharField(default='', max_length=1000)),
                ('current_stock', models.CharField(max_length=1000)),
                ('sku', models.CharField(default='', max_length=1000)),
                ('meta_title', models.CharField(default='', max_length=1000)),
                ('meta_description', models.CharField(default='', max_length=1000)),
                ('thumbnail_img', models.CharField(max_length=10000)),
                ('photos', models.CharField(max_length=100000)),
            ],
        ),
    ]
