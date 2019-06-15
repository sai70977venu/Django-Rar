from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'Sai Venu'})

def add(request):
    x = request.POST['num1']
    y = request.POST['num2']
    s = int(x) + int(y)
    return render(request, 'result.html', {'sum' : s})