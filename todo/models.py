from django.db import models

# Create your models here.

class Item(models.Model):
    name = model.CharField(max_length=50, null=False, blank=False)
    done= model.BooleanField(null=False, blank=False, default=False)

