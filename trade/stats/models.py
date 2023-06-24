from django.db import models
from django.utils.text import slugify
# Create your models here.

class Statistic(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True) # a urls path to the statistic data
    
    @property
    def data(self):
        return self.dataitem_set.all()
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)


class DataItem(models.Model):
    Statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)
    value = models.SmallIntegerField()
    owner = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.owner}: {self.value}"
    