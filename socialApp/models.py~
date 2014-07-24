from django.db import models

class Profile(models.Model):
    email = models.EmailField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    password = models.CharField(max_length=30)
    followers = models.ManyToManyField('self',related_name='Followers', blank=True, null=True, symmetrical=False)
    followings=models.ManyToManyField('self',related_name='Followings', blank=True, null=True, symmetrical=False)
    def __unicode__(self):
        return self.email

