from django.db import models

class Mywebsites(models.Model):
    text = models.TextField()
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,null=True)
    birthday = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    address_local = models.CharField(max_length=200,null=True)
    address_permanent = models.CharField(max_length=200,null=True)
    subject = models.CharField(max_length=200,null=True)

    
    def __str__(self):
        return self.first_name+'-'+self.last_name+'-'+self.birthday