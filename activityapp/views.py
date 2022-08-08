from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from datetime import datetime ,time
from django.utils import timezone
import pytz

timezone = pytz.timezone('Asia/Kolkata')

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['Adm_id'] = user.id
            return redirect('admin_dashboard')

        elif user_registration.objects.filter(username=request.POST['user'], password=request.POST['pass']).exists():
            users = user_registration.objects.get(
                username=request.POST['user'], password=request.POST['pass'])
            request.session['u_id'] = users
            request.session['username'] = users.username
            request.session['u_id'] = users.id
            users = user_registration.objects.filter(id=users.id)
            return render(request, 'user_dashboard.html', {'users': users})
    return render(request, 'login.html')

#Admin Section
def admin_logout(request):
    if 'Adm_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def admin_index(request):
    return render(request,'admin_index.html')

def admin_dashboard(request):
    user = user_registration.objects.all()
    return render(request, 'admin_dashboard.html',{'user':user})

def admin_addsalesman(request):
    if request.method == 'POST':
        a=user_registration()
        a.name = request.POST['n']
        a.email = request.POST['e']
        a.username = request.POST['un']
        a.password = request.POST['p']
        a.save()
        return redirect('admin_dashboard')
    return render(request, 'admin_addsalesman.html')

def admin_useractivity(request):
    activity = activitylog.objects.all().order_by('-id')
    activitycount=activitylog.objects.all().count()

    followupcount = activitylog.objects.filter(stage='Follow Up').count()
    signedupcount = activitylog.objects.filter(stage='SignUp').count()
    notintrest = activitylog.objects.filter(stage='Not intrested').count()

    exicutives = user_registration.objects.all()

    return render(request, 'admin_useractivity.html',{'activity':activity,'activitycount':activitycount,'followupcount':followupcount,'signedupcount':signedupcount,'notintrest':notintrest,'exicutives':exicutives})

def admin_userprofile(request,id):
    user=user_registration.objects.get(id=id)
    activity=activitylog.objects.filter(user_id=user).order_by('-id')
    activitycount=activitylog.objects.filter(user_id=user).count()
    return render(request,'admin_userprofile.html',{'user': user,'activity':activity,'activitycount':activitycount})


#############  User Section  #################

def user_logout(request):
    if 'u_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def user_index(request):
    if request.session.has_key('u_id'):
        u_id = request.session['u_id']
    users = user_registration.objects.filter(id=u_id)
    return render(request, 'user_index.html',{'users': users})

def user_dashboard(request):
    if request.session.has_key('u_id'):
        u_id = request.session['u_id']
    users = user_registration.objects.filter(id=u_id)   
    return render(request, 'user_dashboard.html', {'users': users})

def user_addactivity(request):
    if request.session.has_key('u_id'):
        u_id = request.session['u_id']
    users = user_registration.objects.filter(id=u_id)
    al=activitylog()

    

    if request.method == 'POST':
        
        datz= request.POST['nmd']
    
        if not datz:
            datz = None
       
        al.business=request.POST['bn']
        al.typeofbusiness=request.POST['tob']
        al.location=request.POST['l']
        al.metpersonname=request.POST['mpn']
        al.designation=request.POST['d']
        al.phone=request.POST['pn']
        al.stage=request.POST['s']
        al.nextmeetingdate=datz
        al.remark=request.POST['r']
        al.date=datetime.now().date()
        al.time=datetime.now(tz = timezone)
        al.user_id=u_id
        al.save()

   
        return redirect('user_dashboard')
    return render(request, 'user_addactivity.html', {'users': users})