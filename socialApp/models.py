from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from socialEngine.settings import AVATAR_URL



class Profile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    password = models.CharField(max_length=30)
    profile_picture = models.CharField(max_length=30, default="f1.jpg")
    #(path=AVATAR_URL,match=r'\.jpg$', recursive=False, default="f1.jpg")
    def __unicode__(self):
        return unicode(self.email)

class Pub(models.Model):
    profile = models.ForeignKey(Profile)
    pub_text = models.CharField(max_length=350)
    pub_date = models.DateTimeField(auto_now=True, null=True)
    def __unicode__(self):
        return unicode(self.pub_date.total_seconds())
   
class Follower(models.Model):
    followed = models.ForeignKey(Profile, related_name='profile_followed')
    followers = models.ForeignKey(Profile)
    def __unicode__(self):
        return unicode(self.followed)
        

