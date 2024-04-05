from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class MyModel(models.Model):
    Item_name = models.CharField(max_length=200)
    Quant_ity = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for your profile
    bio = models.TextField(blank=True)
    # Add more fields as needed

    def str(self):
        return self.user.username