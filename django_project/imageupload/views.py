from django.shortcuts import render

from django.http import (
	HttpResponse,
	HttpResponseRedirect,
	Http404,
)
from django.core.urlresolvers import reverse

from imageupload.models import UploadImage
from imageupload.forms import UploadImageForm

# Create your views here.
def index(request):
	return HttpResponse("Temp index page - will be login.")

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