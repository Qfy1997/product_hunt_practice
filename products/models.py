from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50,default='例:抖音-记录美好生活')
    intro = models.TextField(default='在这里写app介绍')
    url   = models.CharField(max_length=100,default='Http://')
    icon  = models.ImageField(default='default_icon.png',upload_to='images/')
    image = models.ImageField(default='default_image.png',upload_to='images/')
    votes = models.IntegerField(default=1)
    pub_date =models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)   # 外键 与用户连锁  用户没了他也没了

    def __str__(self):
        return self.title
