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
    def __unicode__(self):
        return self.email
 
class Pub(models.Model):
    profile = models.ForeignKey(Profile)
    pub_text = models.CharField(max_length=350)
    pub_date = models.DateTimeField(auto_now=True, null=True)
    def __unicode__(self):
        return self.pub_text

class Follower(models.Model):
    followed = models.ForeignKey(Profile, related_name='profile_followed')
    followers = models.ForeignKey(Profile)
