from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import date
class Catigories(models.Model):
     name = models.CharField(max_length=200)
     
     def __str__(self):
         return self.name
     

class Brand(models.Model):
     name = models.CharField(max_length=200)
     def __str__(self):
         return self.name

class Color(models.Model):
     name = models.CharField(max_length=200)
     code = models.CharField(max_length=50)

     def __str__(self):
         return self.name
     


class Filter_Price(models.Model):
     Filter_Price=(
        ('30 TO 70','30 To 70'),
        ('70 TO 100', '70 To 100'), 
          ('100 TO 500','100 TO 500'),
           ('500 TO 700','500 TO 700'),
            ('700 TO 1000','700 TO 1000'),
             ('1000 TO 1200','1000 TO 1200'),
              ('1200 TO 2000','1200 TO 2000'),
              ('2000 TO 2500','2000 TO 2500'),
     )
     price = models.CharField(choices=Filter_Price,max_length=60)  


     def __str__(self):
         return self.price  

class Product(models.Model):
     CONDITION = (('New','New'),('Old','Old'))
     STOCK=(('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK'))
     STATUS=(('Publish','Publish'),('Draft','Draft'))

     unique_id = models.CharField(unique=True,max_length=200,null=True,blank=True)
     image =models.ImageField(upload_to='product_images/img')
     name = models.CharField(max_length=200)
     price= models.IntegerField()
     condition = models.CharField(choices=CONDITION,max_length=100)
     information =RichTextField(null=True)
     description =RichTextField(null=True)
     stock = models.CharField(choices=STOCK,max_length=200)
     status = models.CharField(choices=STATUS,max_length=200)
     craeted_date = models.DateTimeField(default=timezone.now)
     catigories =models.ForeignKey(Catigories,on_delete=models.CASCADE) 
     brand =models.ForeignKey(Brand,on_delete=models.CASCADE) 
     color =models.ForeignKey(Color,on_delete=models.CASCADE) 
     filter_price =models.ForeignKey(Filter_Price,on_delete=models.CASCADE) 


     def save(self,*args,**kwargs):
      if self.unique_id is None and self.craeted_date and self.id:
          self.unique_id = self.craeted_date.strftime('75%Y%m%d23') + str(self.id)
      return super().save(*args,**kwargs)   
     
     def __str__(self):
         return self.name

class Images(models.Model):
    image = models.ImageField(upload_to='product_images/img')
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
         return self.image.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
         return self.name
    
class Contact_us(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    date = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
         return self.email
    

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contry= models.CharField(max_length=100)
    address=models.TextField()
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    postcode= models.IntegerField()
    phone=models.IntegerField()
    email= models.CharField(max_length=100)
    additional_info=models.TextField()
    amount=models.CharField(max_length=100)
    date= models.DateField(default=date.today)
    payment_id = models.CharField(max_length=300,null=True,blank=True)
    paid = models.BooleanField(default= False ,null= True)

    def __str__(self):
      return self.user.username
    
class OrderItem(models.Model):    
    order= models.ForeignKey(Order,on_delete=models.CASCADE,null=True) 
    product= models.CharField(max_length=100)
    image= models.ImageField(upload_to="product_images/Order_Img")
    quantity= models.CharField(max_length=100)
    price= models.CharField(max_length=100)
    total= models.CharField(max_length=1000)
    def __str__(self):
      return self.order.user.username
    
    