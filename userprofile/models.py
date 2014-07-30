from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    def __unicode__(self):
        return self.email
    
User.profile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])
