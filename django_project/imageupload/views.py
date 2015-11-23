from django.shortcuts import render

from django.http import (
	HttpResponse,
	HttpResponseRedirect,
	Http404,
)
from django.core.urlresolvers import reverse

from django.contrib.auth import (
	authenticate,
	login,
	logout,
)
from django.contrib.auth.decorators import login_required


from imageupload.models import (
	Upload,
	UploadImage,
)
from imageupload.forms import (
	UserRegisterForm,
	UploadImageForm,
)


@login_required
def index(request):
	user = request.user

	images = UploadImage.objects.filter(upload__user=user)

	return render(request, 'imageupload/index.html', {'images': images})


def user_login(request):
	if request.method == 'POST':
		if str(request.POST.get('auth_type')) == 'login':
			return handle_login(request)

		# Register
		else:
			return handle_register(request)

	else:
		register_form = UserRegisterForm(prefix='user')

	ctx = {'register_form': register_form}

	return render(request, 'imageupload/login.html', ctx)


def handle_login(request):
	username = str(request.POST['username'])
	password = str(request.POST['password'])

	auth_user = authenticate(username=username, password=password)

	if auth_user:
		login(request, auth_user)

		return HttpResponseRedirect(reverse('index'))

	else:
		error_msg = 'Invalid login details.'
		register_form = UserRegisterForm(prefix='user')
		return render(request, 'imageupload/login.html', {'register_form': register_form, 'error_msg': error_msg})

def handle_register(request):
	form = UserRegisterForm(request.POST, prefix='user')
	if form.is_valid():
		user = form.save()
		user.set_password(user.password)
		user.backend = 'django.contrib.auth.backends.ModelBackend' #hack - apologies!
		user.save()

		auth_user = authenticate(username=user.username, password=user.password)
		login(request, user)

		return HttpResponseRedirect(reverse('index'))

	else:
		print form.errors
		return render(request, 'imageupload/login.html', {'register_form': form})

def handle_logout(request):
	logout(request)

	return HttpResponseRedirect(reverse('index'))


@login_required
def upload(request):
	if request.method == 'POST':
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			new_upload = Upload(user = request.user)
			new_upload.save()

			new_image = UploadImage(upload = new_upload, image = request.FILES['image'])
			new_image.save()

			return HttpResponseRedirect(reverse('upload_result', kwargs={'ui_id': new_image.pk}))
	else:
		form = UploadImageForm()

	return render(request, 'imageupload/upload.html', {'form': form})


@login_required
def upload_result(request, ui_id):
	try:
		upload_image = UploadImage.objects.get(pk=ui_id)
	except UploadImage.DoesNotExist:
		raise Http404("Upload does not exist")

	return render(request, 'imageupload/upload_result.html', {'upload_image': upload_image})

