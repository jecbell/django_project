from django.shortcuts import render

from django.http import (
	HttpResponse,
	HttpResponseRedirect,
	Http404,
)
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from imageupload.models import UploadImage
from imageupload.forms import (
	UserForm,
	UploadImageForm,
)


@login_required
def index(request):
	return HttpResponse("Temp index page - will be login.")
	# if request.method == 'POST':
	# 	form = UserForm(request.POST, prefix='user')
	# 	if form.is_valid():
	# 		user = form.save()
	# 		user.set_password(user.password)
	# 		user.save()

	# 		auth_user = authenticate(username=user.username, password=user.password)
	# 		login(request, user)
	# 	else:
	# 		print form.errors
	# else:
	# 	if not request.user.is_authenticated():
	# 		form = UserForm(prefix='user')
	# 	else:
	# 		pass

	# return render(request, 'imageupload/index.html', {'form': form})

def login(request):
	if request.method == 'POST':
		form = UserForm(request.POST, prefix='user')
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()

			auth_user = authenticate(username=user.username, password=user.password)
			login(request, user)

			return HttpResponseRedirect(reverse('index'))

		else:
			print form.errors

	else:
		form = UserForm(prefix='user')

	return render(request, 'imageupload/login.html', {'form': form})


def upload(request):
	# Handle file upload
		if request.method == 'POST':
			form = UploadImageForm(request.POST, request.FILES)
			if form.is_valid():
				newimage = UploadImage(image = request.FILES['image'])
				newimage.save()

				# Redirect to the upload results after POST
				return HttpResponseRedirect(reverse('upload_result', kwargs={'ui_id': newimage.pk}))
		else:
			form = UploadImageForm() # A empty, unbound form

		return render(request, 'imageupload/upload.html', {'form': form})

def upload_result(request, ui_id):
	try:
		upload_image = UploadImage.objects.get(pk=ui_id)
	except UploadImage.DoesNotExist:
		raise Http404("Upload does not exist")

	return render(request, 'imageupload/upload_result.html', {'upload_image': upload_image})