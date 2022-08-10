from django.db import models
import datetime
from django.utils import timezone

class Soru(models.Model):
    soru_metni = models.CharField(max_length=200)
    yayim_tarihi = models.DateTimeField('yayınlanma tarihi')
    def __str__(self):
          return self.soru_metni

    def was_published_recently(self):
        return self.yayim_tarihi >= timezone.now() - datetime.timedelta(days=1)      


class Secim(models.Model):
    soru = models.ForeignKey(Soru, on_delete=models.CASCADE)
    secim_metni = models.CharField(max_length=200)
    oylar = models.IntegerField(default=0)
    def __str__(self):
          return self.secim_metni
  

  