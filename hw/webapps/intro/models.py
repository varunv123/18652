from django.db import models

# Create your models here.

class Message(models.Model):
	text = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100)
	time = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.text
