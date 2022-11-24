from django.shortcuts import redirect, render
from CRUDOperation.models import EmpModel, Patient
from django.contrib import messages
from CRUDOperation.forms import Empforms, PatientForms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def editpatient(request,id):
    editempobj = Patient.objects.get(id=id)
    return render(request, 'editpatients.html', {"EmpModel":editempobj})


def updatepatient(request,id):
    Updateemp = Patient.objects.get(id=id)
    form = PatientForms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,"Record is updated successfully")
        return render(request, 'editpatients.html', {"EmpModel":Updateemp})

def insertpatient(request):
    if request.method == "POST":
        if request.POST.get('dateofbirth') and request.POST.get('iin') and request.POST.get('fullname') and request.POST.get('bloodgroup') and request.POST.get('emergency_number') and request.POST.get('contact') and request.POST.get('address') and request.POST.get('marital') and request.POST.get('registration'):
            saverecord = Patient()
    
            saverecord.dateofbirth = request.POST.get('dateofbirth')
            saverecord.iin = request.POST.get('iin')
            saverecord.fullname = request.POST.get('fullname')
            saverecord.bloodgroup = request.POST.get('bloodgroup')
            saverecord.emergency_number = request.POST.get('emergency_number')
            saverecord.contact = request.POST.get('contact')
            saverecord.address = request.POST.get('address')
            saverecord.marital = request.POST.get('marital')
            saverecord.registration = request.POST.get('registration')
            saverecord.save()
            messages.success(request, "Patient " + saverecord.fullname + " has been added successfully")
            return render(request, 'insertpatients.html')
    else:
        return render(request, 'insertpatients.html')
 
def doctortable(request):
    showdoctors = EmpModel.objects.all()
    return render(request,'doctortable.html',{"data":showdoctors})

def showspecialization(request):
    spec = EmpModel.objects.all()
    return render(request, 'showspecialization.html',{"data":showspecialization})

def showemp(request):
    showall = EmpModel.objects.all()
    showallpatients = Patient.objects.all()
    return render(request,'index.html',{"data":showall, "patdata":showallpatients})

def insertemp(request):
    if request.method == "POST":
        if request.POST.get('empname') and request.POST.get('dateofbirth') and request.POST.get('iin') and request.POST.get('contact') and request.POST.get('departmentid') and request.POST.get('specializationid') and request.POST.get('experience') and request.POST.get('photo') and request.POST.get('category') and request.POST.get('price') and request.POST.get('schedule') and request.POST.get('education') and request.POST.get('rating') and request.POST.get('address'):
            saverecord = EmpModel()
            saverecord.empname = request.POST.get('empname') 
            saverecord.dateofbirth = request.POST.get('dateofbirth')
            saverecord.iin = request.POST.get('iin')
            saverecord.contact = request.POST.get('contact')
            saverecord.departmentid = request.POST.get('departmentid')
            saverecord.specializationid = request.POST.get('specializationid')
            saverecord.experience = request.POST.get('experience')
            saverecord.photo = request.POST.get('photo')
            saverecord.category = request.POST.get('category')
            saverecord.price = request.POST.get('price')
            saverecord.schedule = request.POST.get('schedule')
            saverecord.education = request.POST.get('education')
            saverecord.rating = request.POST.get('rating')
            saverecord.address = request.POST.get('address')
            saverecord.save()
            messages.success(request, "Doctor " + saverecord.empname + " has been added successfully")
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

def editemp(request,id):
    editempobj = EmpModel.objects.get(id=id)
    return render(request, 'edit.html', {"EmpModel":editempobj})


def updateemp(request,id):
    Updateemp = EmpModel.objects.get(id=id)
    form = Empforms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,"Record is updated successfully")
        return render(request, 'edit.html', {"EmpModel":Updateemp})


def delemp(request,id):
    delemployee = EmpModel.objects.get(id=id)
    delemployee.delete()
    showdata = EmpModel.objects.all()
    return render(request, "delete.html", {"data":showdata})

def delpatient(request,id):
    delemployee = Patient.objects.get(id=id)
    delemployee.delete()
    showdata = Patient.objects.all()
    return render(request, "deletepatients.html", {"data":showdata})

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = EmpModel.objects.all().filter(empname__contains=search)
        education_search = request.GET.get('search')
        post1 = EmpModel.objects.all().filter(empname__contains=education_search)
        specialization_search = request.GET.get('search')
        post2 = EmpModel.objects.all().filter(empname__contains=specialization_search)
        return render(request, 'searchbar.html', {"post": post,"post1":post1,"post2":post2})

def searchbarproc(request):
    if request.method == 'GET':
        search = request.GET.get('search')           
        post = EmpModel.objects.all().filter(education=search)
        return render(request, 'searchbarProc.html', {"post": post})
        

def searchbarspec(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = EmpModel.objects.all().filter(specializationid=search)
        return render(request, 'searchbarSpec.html', {"post": post})