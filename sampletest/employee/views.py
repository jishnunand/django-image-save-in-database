from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

class EmployeeView(View):



    def get(self, request, *args, **kwargs):
    	return render(request, 'index.html')

    def post(self, request):
    	print(request.POST)
    	return HttpResponse("hello")
    	