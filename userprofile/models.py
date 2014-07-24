from django.db import models
from django.contib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
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

User.profile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])
