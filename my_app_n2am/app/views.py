from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    obj=Member.objects.all()
    context={
        "obj":obj,
    }
    return render(request,"index.html",context)