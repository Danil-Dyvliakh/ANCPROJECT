from django.shortcuts import render
from .models import People


# Create your views here.
def first_page(request):
    object_list = People.objects.all()
    return render(request, './index.html', {'object_list': object_list})
