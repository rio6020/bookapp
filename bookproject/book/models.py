from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    purchase_date = models.DateField()
    read_date = models.DateField(null=True,blank=True)
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
