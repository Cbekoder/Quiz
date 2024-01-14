from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    ism = models.CharField(max_length=30, null=True)
    yosh = models.PositiveSmallIntegerField(null=True)
    kasb = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username