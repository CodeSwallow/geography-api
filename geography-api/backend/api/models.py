from django.db import models

# Create your models here.
class USState(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    abbreviation = models.CharField(max_length=2, null=True, blank=True)
    population = models.PositiveIntegerField(null=True, blank=True)
    flag_image = models.ImageField()

    def __str__(self):
        return f"{self.name}, {self.nickname}"
