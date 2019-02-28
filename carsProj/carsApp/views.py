from django.shortcuts import render
from .models import NewCar
from .forms import NewCarForm


# Create your views here.


def index(request):
    allCars = NewCar.objects.all()
    carForm = NewCarForm()
    context = {
        'carForm': carForm,
        'allCars': allCars
    }
    return render(request, 'carsApp/index.html', context)
