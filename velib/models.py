from django.db import models

# Create your models here.
class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    num_bikes = models.SmallIntegerField(default=0)
    bikes_available = models.SmallIntegerField(default=0)
    docks_available = models.SmallIntegerField(default=0)
    capacity = models.SmallIntegerField(default=0)
    is_renting = models.BooleanField()
    is_installed = models.BooleanField()
    is_returning = models.BooleanField()
    commune = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name + " - " + self.commune
