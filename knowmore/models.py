from django.db import models


class Ourteams(models.Model):
    image =  models.ImageField(null=True,blank=True,default='default.jpg')
    name = models.CharField(max_length=200, null=True)
    role  = models.CharField(max_length=200, null=True)
    link  = models.CharField(max_length=200, null=True,blank=True)
    def  __str__(self):
        return self.name
    
class Ourwork(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, default='default.jpg')
    description = models.TextField(null=True, blank=True)
    venue = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)  
    date = models.DateField(null=True, blank=True)

    def  __str__(self):
        return self.title



