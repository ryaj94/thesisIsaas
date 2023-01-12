from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, student_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from joblib import load
model = load('./../saveModels/model.joblib')



from .models import *
from .forms import CreateUserForm

# Create your views here.
@login_required(login_url='loginPage')
@student_only
def home(request):
    userprof = request.user.studentprof
    context = {'userprof': userprof}
    return render(request, 'accounts/StudentProfile.html' , context)

@login_required(login_url='loginPage')
@student_only
def studadvise(request):
    userprof1 = request.user.studentprof
    
    if( userprof1.user_yrandsec == '101' ):
         usergrade = request.user.studentgrades
         arr=[[113,usergrade.gned11], [115,usergrade.dcit21], [116,usergrade.dcit22]]    
         rows, cols = (3, 2)
    elif( userprof1.user_yrandsec == '102' ):
         usergrade = request.user.fy2ndsem
         usergrade1 = request.user.studentgrades
         arr=[[126,usergrade.dcit23],[132,usergrade1.gned11]]    
         rows, cols = (2, 2)
    elif( userprof1.user_yrandsec == '201' ):
         usergrade = request.user.sy1stsem
         arr=[[216,usergrade.dcit24],[215,usergrade.itec55],[217,usergrade.dcit50]]    
         rows, cols = (3, 2)
    elif( userprof1.user_yrandsec == '202' ):
         usergrade = request.user.sy2ndsem
         arr=[[223,usergrade.itec60]]    
         rows, cols = (1, 2)
    elif( userprof1.user_yrandsec == '203' ):
         usergrade = request.user.sysummer
         usergrade1 = request.user.sy2ndsem
         usergrade2 = request.user.sy1stsem
         arr=[[232,usergrade.itec60], [225,usergrade1.dcit55], [235,usergrade2.itec55] ]    
         rows, cols = (3, 2)
    elif( userprof1.user_yrandsec == '301' ):
         usergrade = request.user.ty1stsem
         usergrade1 = request.user.studentgrades
         usergrade2 = request.user.sysummer
         arr=[[311,usergrade.itec80], [312,usergrade.itec85], [313,usergrade.itec90], [315,usergrade.dcit26], [316,usergrade.dcit60], [231,usergrade2.stat2] ]    
         rows, cols = (6, 2)
    elif( userprof1.user_yrandsec == '302' ):
         usergrade = request.user.ty2ndsem
         usergrade1 = request.user.sy2ndsem
         usergrade2 = request.user.sysummer
         arr=[[223,usergrade1.itec60], [232,usergrade2.itec75], [325,usergrade.itec100], [327,usergrade.itec200a] ]    
         rows, cols = (4, 2)
    elif( userprof1.user_yrandsec == '401' ):
         usergrade1 = request.user.ty1stsem
         usergrade = request.user.fy1stsem
         arr=[[312,usergrade1.itec85], [315,usergrade1.dcit26]]    
         rows, cols = (2, 2)



    subj=[]
    for f in range(rows):
        subj.append(model.predict([arr[f]]))

    print(subj)

    context = {'usergrade': usergrade, 'userprof': userprof1, 'subj':subj }
    return render(request, 'accounts/student advising.html', context )


def viewstudents(request):
    studentprofs = studentprof.objects.all()
    print(studentprofs)
   #context = {'studentprof': studentprofs } 
   
    return render(request, 'accounts/ViewStudent.html', {'studentprofs': studentprofs})



def studentinfo(request, pk):
    studinfo = studentprof.objects.get(id=pk)
    context = {'studinfo': studinfo}
    return render(request, 'accounts/StudentInformation.html', context)

def adviserpro2(request):
    adviserprof = request.user.adviserprof
    context = {'adviserprof': adviserprof}
    return render(request, 'accounts/AdviserProfile.html', context)


@unauthenticated_user
def registeruser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)
            studentprof.objects.create(
                user=user
            )
            messages.success(request, "Account successfuly created for "+ username)
            return redirect("home")

    context = {'form': form}
    return render(request, 'accounts/regform.html', context)



@unauthenticated_user
def loginPage(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password incorrect')

     context = {}
     return render(request, 'accounts/index.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def sampleInput(request):
    return render(request, 'accounts/sampleInput.html')

def predict(request):
    rows, cols = (7, 2)
   
    subj=[]
    arr=[]
    for f in range(rows):
        
        subj.append(model.predict([arr[f]]))
        
    print(subj)

    return render(request, 'accounts/sampleOutput.html', {'result': subj})



#@login_required(login_url='loginPage')
#def adminPage(request):
#    return render(request, 'http://127.0.0.1:8000/admin/')    

#def loginstud(request, pk_test):
 #   studentprof1 = studentprof.objects.get(user_id=pk_test)
  #  context = {'studentprof':studentprof1, }
   # return render(request, 'accounts/StudentProfile.html', context)