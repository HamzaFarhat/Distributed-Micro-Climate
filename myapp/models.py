from django.db import models

# Create your models here.
class Conditions(models.Model):
	myId = models.IntegerField()
	location = models.CharField(max_length=200)
	temperature = models.FloatField()
	humidity = models.FloatField()
	windspeed = models.FloatField()
	percipitation = models.FloatField()
	
