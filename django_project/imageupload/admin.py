from django.contrib import admin

from imageupload.models import (
	Upload,
	UploadImage,
)

admin.site.register(Upload)
admin.site.register(UploadImage)