# myapp/views.py

from django.shortcuts import render, redirect
from .forms import DocumentForm


def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})




import requests
from io import BytesIO
from django.http import HttpResponse

# make the HTTP request to get the image file
response = requests.get("http://example.com/image.jpg")

# check if the request was successful
if response.status_code == 200:
    # convert the image file to a bytes object
    image_bytes = BytesIO(response.content)
    # create the HTTP response
    return HttpResponse(image_bytes.read(), content_type="image/jpeg")
else:
    # return an error response
    return HttpResponse("Error retrieving image", status=response.status_code)