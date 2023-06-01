from django.shortcuts import render

# Create your views here.

def genericindex(request):
    return render(request,'genericindex.html')
