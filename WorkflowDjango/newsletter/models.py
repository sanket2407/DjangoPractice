from django.db import models

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=False, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): # Python 3.3. is __str__
		return self.email
		#return str(self.timestamp)