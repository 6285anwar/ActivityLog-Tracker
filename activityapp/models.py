from operator import mod
from django.db import models

class user_registration(models.Model):
    name = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    
class activitylog(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,null=True, blank=True)
    business = models.CharField(max_length=250 ,null=True)
    typeofbusiness = models.CharField(max_length=250 ,null=True)
    location = models.CharField(max_length=250 ,null=True)
    metpersonname = models.CharField(max_length=250 ,null=True)
    designation = models.CharField(max_length=250 ,null=True)
    location = models.CharField(max_length=250 ,null=True)
    phone = models.CharField(max_length=250 ,null=True)
    stage = models.CharField(max_length=250 ,null=True)
    location = models.CharField(max_length=250 ,null=True)
    nextmeetingdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    remark = models.CharField(max_length=250 ,null=True)
    date = models.DateField(null=True, default='0000-00-00', blank=True)
    time = models.TimeField(auto_now_add=False, auto_now=False,  null=True, blank=True)


    def __str__(self):
        return self.typeofbusiness

