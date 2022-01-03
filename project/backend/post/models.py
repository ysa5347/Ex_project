from django.db import models

class Post(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
