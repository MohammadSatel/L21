from django.db import models

# Create your models here.
class Product(models.Model):
    description = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    fields =['desc','price']
 
    def __str__(self):
           return self.description
