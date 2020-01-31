from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from  .models import Product
from .forms import ProductModelForm
# from employee.

# Create your views here.
def xuv(*args,**kwargs):
    return HttpResponse('<h1>hello</h1>')
def ven(request):
    return render(request,'ven.html')

def home(request):
    count = User.objects.count()

    return render(request,'home.html',{'count':count})


def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request,'signup.html',{'form':form})


def upload(request):
    context = {}
    if request.method =='POST':
        uploaded_file = request.FILES['document']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
    return render(request,'upload.html',context)

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = EmployeeSerializer


def product_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    # obj = Product.objects.get(id=1)
    context = {
        'form':form
    }
    return render(request,'products/product_detail.html',context)
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'objects':obj
    }
    return render(request,'products/product_detail.html')
