from django.db import models

class PhotoModel(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100, null=True)
	date = models.DateTimeField(auto_now_add=False)

	def __str__(self):
		return self.title