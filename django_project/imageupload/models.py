from django.db import models
from django.conf import settings

from django.utils import timezone

class Upload(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	upload_date = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.user.username + " " + str(self.upload_date)


class UploadImage(models.Model):
	upload = models.ForeignKey(Upload)
	image = models.ImageField()

	def __unicode__(self):
		return self.image.name
