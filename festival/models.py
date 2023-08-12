from django.db import models

# Create your models here.
class Festival(models.Model):
    contentid = models.CharField(max_length=10)
    contenttypeid = models.CharField(max_length=2)
    title = models.CharField(max_length=200)
    createdtime = models.DateTimeField()
    modifiedtime = models.DateTimeField()
    tel = models.CharField(max_length=20)
    telname = models.CharField(max_length=50)
    homepage = models.URLField()
    booktour = models.TextField(blank=True)
    firstimage = models.URLField()
    firstimage2 = models.URLField()
    cpyrhtDivCd = models.CharField(max_length=10)
    areacode = models.CharField(max_length=5)
    sigungucode = models.CharField(max_length=5)
    cat1 = models.CharField(max_length=10)
    cat2 = models.CharField(max_length=10)
    cat3 = models.CharField(max_length=10)
    addr1 = models.CharField(max_length=200)
    addr2 = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    mapx = models.CharField(max_length=20)
    mapy = models.CharField(max_length=20)
    mlevel = models.CharField(max_length=2)
    overview = models.TextField()

    def __str__(self):
        return self.title