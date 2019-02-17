from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
from django.views import View

from employee.models import Employee
import base64

class EmployeeView(View):



    def get(self, request, *args, **kwargs):
    	return render(request, 'index.html')

    def post(self, request):
    	if request.method == "POST":
    		employee_fname = request.POST.get('employee_fname')
    		employee_lname = request.POST.get('employee_lname')
    		employee_email = request.POST.get('employee_email')
    		employee_phone = request.POST.get('employee_phone')
    		employee_gender = request.POST.get('employee_gender')
    		employee_image = request.POST.get('something')
    		format, imgstr = employee_image.split(';base64,')
    		try:
    			user = User()
    			user.email = employee_email
    			user.first_name = employee_fname
    			user.last_name = employee_lname
    			user.username = employee_email
    			user.save()
    			emp = Employee()
    			emp.employee_image = base64.decodebytes(imgstr)
    			emp.employee_gender = employee_gender
    			emp.user = user
    			emp.image_link = "%s%s" % (format, ";base64,")
    			emp.save()
    		except Exception as e:
    			print(e)
    	return HttpResponse("hello")
    	