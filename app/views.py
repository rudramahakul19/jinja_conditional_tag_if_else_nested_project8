from django.shortcuts import render

# Create your views here.

def condition(request):
     d={'a':1000, 'b':2000, 'c':10000}
     return render(request,'condition.html',d)

