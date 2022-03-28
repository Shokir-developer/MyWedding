from django.shortcuts import render
from .models import PhotoModel
def index(request):
	context = {}
	return render(request, 'index.html', context)


def photos(request):

	elements = PhotoModel.objects.all()

	context = {'elements':elements}
	return render(request, 'photos.html', context)