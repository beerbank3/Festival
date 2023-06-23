from django.db import models

# Create your models here.
### 나라
class Country(models.Model):
    name = models.CharField(max_length=30)