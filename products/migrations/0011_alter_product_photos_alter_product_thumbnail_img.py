# Generated by Django 4.0 on 2023-03-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_photos_alter_product_thumbnail_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photos',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail_img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]