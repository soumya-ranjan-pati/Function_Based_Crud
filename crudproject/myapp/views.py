import email
from unicodedata import name
from django.shortcuts import render,redirect

from myapp.models import Employee
from django.contrib import messages


def index(request):
      return render(request,'myapp/index.html')
      
def register(request):
      return render(request,'myapp/register.html')  


def save(request):
      id=request.POST.get('t1')
      na=request.POST.get('t2')
      con=request.POST.get('t3')
      em=request.POST.get('t4')
      sal=request.POST.get('t5')
      adr=request.POST.get('t6')
      Employee(idno=id,name=na,contact=con,email=em,salary=sal,address=adr).save()
      messages.success(request,'Employee Details Are Saved')
      return redirect('register')

def details(request):
      result=Employee.objects.all()
      return render(request,'myapp/details.html',{'data':result})   

def update(request):
      idno=request.GET.get('no')
      result=Employee.objects.get(idno=idno)
      return render(request,'myapp/update.html',{'data':result})  

def update_data(request):
      id=request.POST.get('t1')
      na=request.POST.get('t2')
      con=request.POST.get('t3')
      em=request.POST.get('t4')
      sal=request.POST.get('t5')
      adr=request.POST.get('t6')
      Employee.objects.filter(idno=id).update(name=na,contact=con,email=em,salary=sal,address=adr)
      messages.success(request,'Employee Details Are Updated')
      return redirect('details')

def delete(request):
      idno=request.GET.get('no')
      Employee.objects.filter(idno=idno).delete()
      messages.success(request,'Employee Details Are Deleted')
      return redirect('details')  

def login(request):
      return render(request,'myapp/login.html')      

def login_page(request):
      em=request.POST.get('s1')
      na=request.POST.get('s2')
      try:
            result=Employee.objects.get(email=em,name=na)          
            return render(request,'myapp/loginpage.html',{"data1":result})
      except Employee.DoesNotExist:
            messages.error(request,'Invalid Username And Emailid')
            return redirect('login')
                   

