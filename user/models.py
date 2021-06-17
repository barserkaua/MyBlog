
from django.db import models
from django.contrib.auth.models import User


class Ownable(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=("Author"),
                             related_name="%(class)ss", on_delete=models.CASCADE)

    class Meta:
        abstract = True


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tracking = models.ManyToManyField('self',
                                      related_name='tracked_by',
                                      blank=True, symmetrical=False)


class FeedItem(Ownable):
    content = models.CharField("Content", max_length=1000,
                               blank=True, null=True)