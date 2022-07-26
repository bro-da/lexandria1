



# Create your models here.
from security.models import category
from django.urls import reverse
from django.db import models
from django.forms import SlugField


# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug        =models.SlugField(max_length=200,unique=True)
    description =models.TextField(max_length=500,blank=True) 
    price       =models.IntegerField()
    images      =models.ImageField(upload_to='photos/products')    
    stock       =models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('products_by_main_category',args=[self.slug])

    def get_urls(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

