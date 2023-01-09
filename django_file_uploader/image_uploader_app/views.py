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
