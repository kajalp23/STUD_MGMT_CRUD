from django.shortcuts import render,get_object_or_404
from student.models import Stud
from student.forms import studReg

# Create your views here.

# def get(self, request, mail, template_name='modifyPatient.html'):
#         thatPatient = Patient.objects.filter(email=mail)
#         thatPatient = thatPatient[0]
#         args = {}
#         args["pat"] = thatPatient
#         return render(request, template_name, args)

#     def post(self, request, mail, template_name='modifyPatient.html'):
#         currentStatus = request.POST.get('currentStatus')
#         remarks = request.POST.get('remarks')
#         ventilator = request.POST.get('ventilator')
#         if ventilator == "No":
#             ventilator = False
#         else:
#             ventilator = True
#         operatedByDoctor = request.POST.get('operatedByDoctor')
#         Patient.objects.filter(email=mail).update(currentStatus=currentStatus, remarks=remarks, ventilator=ventilator, operatedByDoctor=operatedByDoctor)
#         return render(request, template_name, {"errorMessage": "Changes Done Successfully"})


def update(request,up_id):
    if request.method=="POST":
        fm = studReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            Stud.objects.filter(id=up_id).update(name=nm,email=em,password=ps)
            fm = studReg()
            fobj=Stud.objects.all()
            err_msg = {'msg':'Student Updated Successfully','form':fm,'mobj':fobj}

            return render(request,'index.html',err_msg)
    else:
        thatStu = Stud.objects.filter(id=up_id)
        thatStu = thatStu[0]
        fob = Stud.objects.all()
        args = {"form":thatStu,'mobj':fob}
        return render(request,'student/update.html',args)
    



def delete(request,my_id):
    inst = Stud.objects.get(id=my_id)
    inst.delete()
    fobj = Stud.objects.all()
    fm = studReg()
    err_msg = {'msg':'Student is Deleted Successfully','form':fm,'mobj':fobj}
    return render(request,'index.html',err_msg)
    
