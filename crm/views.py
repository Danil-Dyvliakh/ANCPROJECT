from django.shortcuts import render
from .models import People
from .forms import PeopleForm


# Create your views here.
def first_page(request):
    object_list = People.objects.all()
    form = PeopleForm()

    return render(request, './index.html', {'object_list': object_list,
                                            'form': form})


def thanks_page(request):
    name = request.POST.get("name")
    position = request.POST.get('position' , 'position')
    email = request.POST.get('email', 'email')
    element = People(order_name = name, order_position = position, order_email = email)
    element.save()
    return render(request, './thanks_page.html', { 'name': name,
                                                  'position': position,
                                                  'email': email})
