from django.db import models

class UploadFile(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='store/cover')
	pdf = models.FileField(upload_to='store/pdf')

	def __str__(self):
		return self.name
