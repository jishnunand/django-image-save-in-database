from django.shortcuts import render

# Create your views here.
from num2words import num2words
from django.http import HttpResponse


def number_to_word(request):
    if request.method == "POST":
        number = request.POST.get('number')
        numm = num2words(number)
        return HttpResponse(numm)
    else:
        return render(request, 'number.html')

def home(request):
    return render(request, 'main.html')