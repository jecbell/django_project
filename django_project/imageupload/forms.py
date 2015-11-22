from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from PIL import Image
from cStringIO import StringIO

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class UploadImageForm(forms.Form):
	image = forms.ImageField(
		label='Select an image file',
	)

	def clean_image(self):
		pillow_image = self.cleaned_data['image'].image
		errors = []

		if pillow_image.format != 'PNG':
			errors.append(
				ValidationError(
					'Image format: %s -  must be .png' % pillow_image.format,
					code='invalid_file_format'
				)
			)

		if pillow_image.size != (200,300):
			errors.append(
				ValidationError(
					'Image size: (%d, %d) - must be 200 x 300' % pillow_image.size,
					code='invalid_image_size'
				)
			)


		n_colours = len(set([colour for colour in Image.open(self.cleaned_data['image'].file).getdata()]))

		if n_colours != 2:
			errors.append(
				ValidationError(
					'Number of image colours: %d - must be 2' % n_colours,
					code='invalid_image_size'
				)
			)


		if len(errors):
			raise ValidationError(errors)
