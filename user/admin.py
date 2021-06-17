
from django.contrib import admin

# Register your models here.
from user.models import RegisteredUser

admin.site.register(RegisteredUser)