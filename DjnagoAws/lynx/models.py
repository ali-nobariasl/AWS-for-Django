from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default='bird.jpg', upload_to= 'images/')

    ## upload_to= 'images/' is defines the folder in aws which images will be uploaded