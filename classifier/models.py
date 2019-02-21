from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Image(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(None)
    date = models.DateField(default=datetime.today())
    side = models.CharField(max_length=1)
    stage = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})

    def __str__(self):
        return self.image.url

