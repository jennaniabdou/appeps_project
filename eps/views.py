from django.shortcuts import render
from .models import Module, Type


# Create your views here.
def index(request):

	categories = Type.objects.all()
	context = {
		'categories': categories
	}

	return render(request, 'eps/base.html', context)


# Create your views here.


def eps(request):
	return render(request, 'eps/base1.html')
