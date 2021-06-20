from django.contrib.auth.models import User
from django.db import models


# Post model in db
from main.models import RegisteredUser


class Article(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Date publish')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Article: {self.title}'

    def get_absolute_url(self):
        return f'/posts/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Article'
