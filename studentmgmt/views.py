from django.shortcuts import render
from django.core.exceptions import ValidationError
from student.forms import studReg
from student.models import Stud

def index(request):
    fobj = Stud.objects.all()
    if(request.method=="POST"):
        fm = studReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']

            reg = Stud(name=nm,email=em,password=ps)
            reg.save()
            fm = studReg()
            err_msg = {'msg':'Student Added Successfully','form':fm,'mobj':fobj}

            return render(request,'index.html',err_msg)

    else:
        fm = studReg()
        err_msg = {'form':fm,'mobj':fobj}
        return render(request,'index.html',err_msg)
    

    

    