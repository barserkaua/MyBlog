
from django.db import models
from django.contrib.auth.models import User


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tracking = models.ManyToManyField('self',
                                      related_name='tracked_by',
                                      blank=True, symmetrical=False)
