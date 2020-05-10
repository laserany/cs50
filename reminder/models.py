from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone = PhoneField()

class Group(models.Model):
    name = models.TextField(unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    
class Record(models.Model):
    description = models.TextField()
    method = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

class GroupMember(models.Model):
    name = models.TextField()
    phone = PhoneField()
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)