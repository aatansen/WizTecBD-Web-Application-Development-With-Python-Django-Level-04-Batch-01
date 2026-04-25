from django.db import models

# Create your models here.
class ProductModel(models.Model):
  product_name=models.CharField(max_length=100,null=True)
  product_price=models.FloatField(null=True)
  product_description=models.TextField(null=True)
  product_qty=models.PositiveIntegerField(null=True)

  PRODUCT_CATEGORY=[
    ('Electric','Electric'),
    ('Cloth','Cloth'),
    ('Food','Food'),
  ]
  product_cat=models.CharField(choices=PRODUCT_CATEGORY,null=True)
  product_img=models.ImageField(upload_to='media/product_imgs',null=True)

  def __str__(self):
    return f'{self.product_name}'