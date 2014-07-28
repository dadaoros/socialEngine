from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    password = models.CharField(max_length=30)
    user = models.OneToOneField(User)
    followers = models.ManyToManyField('self',related_name='Followers', blank=True, null=True, symmetrical=False)
    followings=models.ManyToManyField('self',related_name='Followings', blank=True, null=True, symmetrical=False)
    def __unicode__(self):
        return self.email
 
class Pub(models.Model):
    profile = models.ForeignKey(Profile)
    pub_text = models.CharField(max_length=350)
    pub_date = models.DateTimeField(auto_now=True, null=True)
    def __unicode__(self):
        return self.pub_text
