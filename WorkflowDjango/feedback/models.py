from django.db import models

# Create your models here.
class FeedBack(models.Model):
	feedback = models.CharField(max_length=120, blank=False, null=True)
	email = models.EmailField()

	def __unicode__(self): # Python 3.3. is __str__
		return self.email