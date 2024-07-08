from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Book(models.Model):

    status_book = [
        ('Available','Available'),
        ('Rental','Rental'),
        ('Sold','Sold'),
    ]
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    book_photo = models.ImageField(upload_to='photos/book_photo' , null=True , blank=True)
    author_photo = models.ImageField(upload_to='photos/author_photo' , null=True , blank=True)
    pages = models.IntegerField(null=True , blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2 , null=True , blank=True)
    rental_price_day = models.DecimalField(max_digits=5, decimal_places=2,null=True , blank=True)
    rental_period = models.IntegerField(null=True,blank=True)
    total_rental = models.DecimalField(max_digits=5,decimal_places=2 , null=True , blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices= status_book , null=True , blank=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT ,null=True , blank=True)
    
    def __str__(self):
        return self.title
