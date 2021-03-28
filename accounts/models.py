from django.db import models

# Create your models here.
class organization(models.Model):

    username = models.CharField(max_length=1000)
    email= models.URLField()
    img= models.ImageField( upload_to='pics',null=True,blank=True)
    # number = models.IntegerField()
    password= models.CharField(max_length=200)
    des = models.TextField()
    cammount=models.IntegerField(null=True,blank=True)
    Dname=models.TextField(null=True,blank=True)
