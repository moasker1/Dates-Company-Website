from django.db import models

class Member(models.Model):
  name      = models.CharField( max_length=22  , null= False ) 
  email     = models.CharField( max_length=101 , null= False )
  password  = models.CharField( max_length=22  , null= False )
  
  def __str__(self):
    return f"{self.name}"



class Category(models.Model):
  title = models.CharField(max_length=50, null=True)

  def __str__(self):
    return f"{self.title}"



class Product(models.Model):
  name     = models.CharField(max_length=255) 
  category   = models.ForeignKey(Category,on_delete=models.CASCADE)
  image = models.ImageField(upload_to='photos/%y/%m/%d' ,null= True, default='photos/23/02/13/def.jpg' )
  brief    = models.TextField(null= True)
  price    = models.DecimalField(max_digits=6 , decimal_places=2)

  def __str__(self):
    return f"{self.name} - {self.category}"





