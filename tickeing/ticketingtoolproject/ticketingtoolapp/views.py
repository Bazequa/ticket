from django.shortcuts import render,HttpResponseRedirect
from .forms import  SelectType,ProductForm,ApplicationForm,BookingForm, SignUpForm,StationaryForm
from .forms import ProductChoiceForm,ApplicationChoiceForm,BookingChoiceForm,StationaryChoiceForm
from .models import ProductModel,ApplicationModel,BookingModel,StationaryModel
# from .models import Manager,Employee,AdminPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        admin_names=['bazequa','ramesh']
        if user is not None:
            if uname=='kalyan':
                login(request, user)
                messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('/manager')
            elif uname in admin_names:
                login(request, user)
                messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('/adminpage')
            else:
                login(request, user)
                messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('/employee')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form':fm})
  else:
        return HttpResponseRedirect('/')
    
def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            fm.save()
            return HttpResponseRedirect("/login/")
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form':fm})

def ulogout(request):

    logout(request)
    return HttpResponseRedirect('/')


def products(request):

    if request.method=='POST':
        fm=ProductForm(request.POST)

        if fm.is_valid():
            messages.success(request, 'data saved')
            model = ProductModel(user=request.user, your_requirement=request.POST.get('your_requirement'), Reason=request.POST.get('Reason'),
            employee_name=request.POST.get('employee_name'), employee_id=request.POST.get('employee_id'),
            request_raised_at=request.POST.get('request_raised_at'))
            model.save()
            
            return HttpResponseRedirect('/employee')
    else:
        fm=ProductForm()
    return render(request,'products.html',{'form':fm})



def application(request):

    if request.method=='POST':
        fm=ApplicationForm(request.POST)

        if fm.is_valid():
            messages.success(request, 'data saved')
            model = ApplicationModel(user=request.user, your_requirement=request.POST.get('your_requirement'), Reason=request.POST.get('Reason'),
            employee_name=request.POST.get('employee_name'), employee_id=request.POST.get('employee_id'),
            request_raised_at=request.POST.get('request_raised_at'))
            model.save()
           
            return HttpResponseRedirect('/employee')
    else:
        fm=ApplicationForm()
    return render(request,'application.html',{'form':fm})

def booking(request):

    if request.method=='POST':
        fm=BookingForm(request.POST)

        if fm.is_valid():
            messages.success(request, 'data saved')
            model = BookingModel(user=request.user, your_requirement=request.POST.get('your_requirement'), Reason=request.POST.get('Reason'),
            employee_name=request.POST.get('employee_name'), employee_id=request.POST.get('employee_id'),
            request_raised_at=request.POST.get('request_raised_at'))
            model.save()
            return HttpResponseRedirect('/employee')
    else:
        fm=BookingForm()
    return render(request,'booking.html',{'form':fm})

def stationary(request):
    if request.method=='POST':
        fm=StationaryForm(request.POST)

        if fm.is_valid():
            messages.success(request,'data saved')
            model=StationaryModel(user=request.user,your_requirement=request.POST.get('your_requirement'),Reason=request.POST.get('Reason'),
            employee_name=request.POST.get('employee_name'),employee_id=request.POST.get('employee_id'),
            request_raised_at=request.POST.get('request_raised_at'))
            model.save()
            return HttpResponseRedirect('/employee')
    else:
        fm=StationaryForm()
    return render(request,'stationary.html',{'form':fm})

def employee(request):
    id='raised'
    pfm=ProductModel.objects.all()
    afm=ApplicationModel.objects.all()
    bfm=BookingModel.objects.all()
    sfm=StationaryModel.objects.all()
    context={'pfm':pfm,'afm':afm,'bfm':bfm,'sfm':sfm,'id':id}
    return render(request,'employee.html',context)

def manager(request):
    id='raised'
    pfm=ProductModel.objects.all()
    afm=ApplicationModel.objects.all()
    bfm=BookingModel.objects.all()
    sfm=StationaryModel.objects.all()
    context = {'pfm': pfm, 'afm': afm, 'bfm': bfm, 'sfm': sfm}
    return render(request,'manager.html',context)

def manager1(request):
    if request.method=="POST":
        print(request.POST)
        pfm1 = ProductChoiceForm(request.POST)
        afm1 = ApplicationChoiceForm(request.POST)
        bfm1 = BookingChoiceForm(request.POST)
        sfm1 = StationaryChoiceForm(request.POST)
        if pfm1.is_valid():
            pfm1.save()
        if afm1.is_valid():
            afm1.save()
        if bfm1.is_valid():
            bfm1.save()
        if sfm1.is_valid():
            sfm1.save()
        context={'pfm1':pfm1,'afm1':afm1,'bfm1':bfm1,'sfm1':sfm1,'id':id}
        return render(request,'manager.html',context)
    else:
        return HttpResponseRedirect('/manager')

def admin(request):
    id='raised'
    pfm=ProductModel.objects.all()
    afm=ApplicationModel.objects.all()
    bfm=BookingModel.objects.all()
    sfm=StationaryModel.objects.all()
    context={'pfm':pfm,'afm':afm,'bfm':bfm,'sfm':sfm,'id':id}
    return render(request,'admin.html', context )

# def reject(request,id, model):
#     # if model==1:
#     #     rpm=ProductModel.objects.get(id=id)
#     #     rpm.reject_status=2
#     #     rpm.save()
#     # if model == 2:
#     #     ram = ApplicationModel.objects.get(id=id)
#     #     ram.reject_status=2
#     #     ram.save()
#     # if model == 3:
#     #     rbm = BookingModel.objects.get(id=id)
#     #     rbm.reject_status=2
#     #     rbm.save()
#     return HttpResponseRedirect('/manager')

# def accept(request,id,model):
#         # value='raised'
#         # if model == 1:
#         #     apm =ProductModel.objects.get(id=id)
#         #     value.replace('accept')
#         #     print(apm)
#         # if model == 2:
#         #     aam=ApplicationModel.objects.get(id=id)
#         #     value.replace('accept')
#         #     print(aam)
#         # if model == 3:
#         #     abm=BookingModel.objects.get(id=id)
#         #     value.replace('accept')
#         #     print(abm)
#         return HttpResponseRedirect('/manager')

def tdelete(request,id,model):
        if model == 1:
            dpm =ProductModel.objects.get(id=id)
            dpm.delete()
        if model == 2:
            dam=ApplicationModel.objects.get(id=id)
            dam.delete()
        if model == 3:
            dbm=BookingModel.objects.get(id=id)
            dbm.delete()
        if model == 4:
            dsm=StationaryModel.objects.get(id=id)
            dsm.delete()
        return HttpResponseRedirect('/employee')


def edit(request,model,id):
    print(type(model))
    if model == 1:
        pmodel=ProductModel.objects.get(id=id)
        pmodel.status = 'accepted'
        pmodel.save(update_fields=['status'])
        return HttpResponseRedirect('/manager')




