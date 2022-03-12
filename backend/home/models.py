from django.conf import settings
from django.db import models


class Homepage(models.Model):
    "Generated Model"
    name = models.IntegerField()
    mobile = models.IntegerField()
