from django.shortcuts import render,HttpResponseRedirect
from .forms import  ProductForm,ApplicationForm,BookingForm, SignUpForm,StationaryForm,TicketForm
from .models import ProductModel,ApplicationModel,BookingModel,StationaryModel,Ticket
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
    return HttpResponseRedirect('/login')


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
    ticketmodel=Ticket.objects.all()
    context={'pfm':pfm,'afm':afm,'bfm':bfm,'sfm':sfm,'id':id,'ticket':ticketmodel}
    return render(request,'employee.html',context)

def manager(request):
    id='raised'
    pfm=ProductModel.objects.all()
    afm=ApplicationModel.objects.all()
    bfm=BookingModel.objects.all()
    sfm=StationaryModel.objects.all()
    ticket=Ticket.objects.all()
    context = {'pfm': pfm, 'afm': afm, 'bfm': bfm, 'sfm': sfm,'ticket':ticket}
    return render(request,'manager.html',context)


def admin(request):
    id='raised'
    pfm=ProductModel.objects.all()
    afm=ApplicationModel.objects.all()
    bfm=BookingModel.objects.all()
    sfm=StationaryModel.objects.all()
    context={'pfm':pfm,'afm':afm,'bfm':bfm,'sfm':sfm,'id':id}
    return render(request,'admin.html', context )


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


def accept(request,model,id):
    # print(type(model))
    if model == 1:
        pmodel=ProductModel.objects.get(id=id)
        pmodel.status = 'accepted'
        pmodel.save(update_fields=['status'])

    if model == 2:
        amodel=ApplicationModel.objects.get(id=id)
        amodel.status= 'accepted'
        amodel.save(update_fields=['status'])

    if model==3:
        bmodel=BookingModel.objects.get(id=id)
        bmodel.status='accepted'
        bmodel.save(update_fields=['status'])

    if model==4:
        smodel=StationaryModel.objects.get(id=id)
        smodel.status='accepted'
        smodel.save(update_fields=['status'])
    
    if model==5:
        tmodel=Ticket.objects.get(id=id)
        tmodel.Status='accepted'
        tmodel.save(update_fields=['Status'])
    
    return HttpResponseRedirect('/manager')

def reject(request,model,id):
    # print(type(model))
    if model == 1:
        pmodel=ProductModel.objects.get(id=id)
        pmodel.status = 'rejected'
        pmodel.save(update_fields=['status'])

    if model == 2:
        amodel=ApplicationModel.objects.get(id=id)
        amodel.status= 'rejected'
        amodel.save(update_fields=['status'])

    if model==3:
        bmodel=BookingModel.objects.get(id=id)
        bmodel.status='rejected'
        bmodel.save(update_fields=['status'])

    if model==4:
        smodel=StationaryModel.objects.get(id=id)
        smodel.status='rejected'
        smodel.save(update_fields=['status'])

    if model==5:
        tmodel=Ticket.objects.get(id=id)
        tmodel.Status='rejected'
        tmodel.save(update_fields=['Status'])
    return HttpResponseRedirect('/manager')

def complete(request,model,id):
    # print(type(model))
    if model == 1:
        pmodel=ProductModel.objects.get(id=id)
        pmodel.status = 'completed'
        pmodel.save(update_fields=['status'])

    if model == 2:
        amodel=ApplicationModel.objects.get(id=id)
        amodel.status= 'completed'
        amodel.save(update_fields=['status'])

    if model==3:
        bmodel=BookingModel.objects.get(id=id)
        bmodel.status='completed'
        bmodel.save(update_fields=['status'])

    if model==4:
        smodel=StationaryModel.objects.get(id=id)
        smodel.status='completed'
        smodel.save(update_fields=['status'])

    if model==5:
        smodel=Ticket.objects.get(id=id)
        smodel.Status='completed'
        smodel.save(update_fields=['Status'])
    return HttpResponseRedirect('/adminpage')

def ticket(request):
    if request.method=='POST':
        fm=TicketForm(request.POST)
        if fm.is_valid():
            model=Ticket(user=request.user,Subject=request.POST.get('Subject'),
            Severity=request.POST.get('Severity'),
            Type=request.POST.get('Type'),
            Manager=request.POST.get('Manager'),
            Remarks=request.POST.get('Remarks'))
            model.save()
        return HttpResponseRedirect('/ticket')
    else:
        fm=TicketForm()
    return render(request,'ticket.html',{'form':fm})

def ticket_id(request,model,id,ticket_no):
    print('===============',id)
    print(model)
    if model==5:
        # a=Ticket.objects.all()
        b=Ticket.objects.get(ticket_no=ticket_no)
        return render(request,'ticket_info.html',{'b':b})


