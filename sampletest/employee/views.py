from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from employee.models import Employee
import base64
from employee.forms import LoginForm, EmployeeForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class EmployeeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()
        return render(request, 'view.html', {'emp': emp})

    def post(self, request):
        if request.method == "POST":
            # print(request.POST)
            # print(request.FILES)
            employee_fname = request.POST.get('employee_fname')
            employee_lname = request.POST.get('employee_lname')
            employee_email = request.POST.get('employee_email')
            employee_phone = request.POST.get('employee_phone')
            employee_gender = request.POST.get('employee_gender')
            employee_address = request.POST.get('employee_address')
            employee_image = request.FILES['employee_image'].file.read()
            ep = base64.b64encode(employee_image)
            # print(employee_image)
            try:
                user = User()
                user.email = employee_email
                user.first_name = employee_fname
                user.last_name = employee_lname
                user.username = employee_email
                user.set_password('@dmin123')
                user.save()
                emp = Employee()
                emp.employee_image = ep
                emp.employee_gender = employee_gender
                emp.user = user
                emp.employee_address = employee_address
                emp.employee_phone = employee_phone

                emp.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect('/emp/')


class Agent(LoginRequiredMixin, View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'add_emp.html', {'form': form})


def login_page(request):
    print(request.user.is_authenticated)
    print(request.path)
    if request.user.is_authenticated:
        return HttpResponseRedirect('/emp/')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.path)
            else:
                print('no login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def employee_details(request, emp_id):
    try:
        emp = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExists:
        emp = None
    return render(request, 'emp_view.html', {'emp': emp})
