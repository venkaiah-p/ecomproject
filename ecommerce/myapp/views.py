from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product
# Create your views here.
@login_required
def index(request):
    p=Product.objects.all()
    context={'p':p}
    return render(request,'index.html',context)