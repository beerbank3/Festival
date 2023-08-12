from django.db import models

# Create your models here.

class Event(models.Model):
    addr1 = models.CharField(max_length=200)
    addr2 = models.CharField(max_length=200)
    booktour = models.CharField(max_length=200)
    cat1 = models.CharField(max_length=10)
    cat2 = models.CharField(max_length=10)
    cat3 = models.CharField(max_length=10)
    contentid = models.CharField(max_length=10, unique=True)
    contenttypeid = models.CharField(max_length=10)
    createdtime = models.DateTimeField()
    eventstartdate = models.DateField()
    eventenddate = models.DateField()
    firstimage = models.URLField()
    firstimage2 = models.URLField()
    cpyrhtDivCd = models.CharField(max_length=10)
    mapx = models.CharField(max_length=20)
    mapy = models.CharField(max_length=20)
    mlevel = models.CharField(max_length=5)
    modifiedtime = models.DateTimeField()
    areacode = models.CharField(max_length=5)
    sigungucode = models.CharField(max_length=5)
    tel = models.CharField(max_length=20)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title