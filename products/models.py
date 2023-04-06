from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300, blank=True)
    category_id = models.CharField(max_length=1000)
    brand_id = models.CharField(max_length=1000, blank=True)
    video_provider = models.CharField(max_length=1000, default="youtube", blank=True)
    video_link = models.CharField(max_length=1000, blank=True)
    tags = models.CharField(max_length=1000, blank=True)
    unit_price = models.CharField(max_length=1000)
    purchase_price = models.CharField(max_length=1000, blank=True)
    unit = models.CharField(max_length=1000, default="pc", blank=True)
    slug = models.CharField(max_length=1000, blank=True)
    current_stock = models.CharField(max_length=1000)
    sku = models.CharField(max_length=1000, blank=True)
    meta_title = models.CharField(max_length=1000, blank=True)
    meta_description = models.CharField(max_length=1000, blank=True)
    thumbnail_img = models.CharField(max_length=100, blank=True)
    photos = models.CharField(max_length=100, blank=True)   

    class Meta:
        db_table = 'products_product'
        managed = True

    def __str__(self):
        return f'{self.name}'



class File(models.Model):
    file = models.FileField(upload_to="files")