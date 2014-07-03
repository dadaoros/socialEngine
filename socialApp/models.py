from django.db import models

class Profile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)
    followers = models.ForeignKey('self',related_name='Followers', blank=True, null=True, on_delete=models.SET_NULL)
    followings=models.ForeignKey('self',related_name='Followings', blank=True, null=True, on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.email

