from django.db import models
from django.db.models import Q


class PdfQuerySet(models.QuerySet):
    def search(self, query=None):
        
        if query is None or query == "":
            return f'No material yet. Check back later {self.none()}'
        lookups = Q(name__icontains=query)
        return self.filter(lookups)

class PdfManager(models.Manager):
    def get_queryset(self):
        return PdfQuerySet(self.model, using=self._db)
    def search(self, query=None):
        return self.get_queryset().search(query=query)



class UploadFile(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='store/cover')
	pdf = models.FileField(upload_to='store/pdf')
	objects = PdfManager()

	def __str__(self):
		return self.name

class SubscribedEmail(models.Model):
	email_name = models.CharField(max_length=120)

	def __str__(self):
		return f'emails'