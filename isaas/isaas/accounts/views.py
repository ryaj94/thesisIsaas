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
    usergrade = request.user.studentgrades
    usergrade1 = request.user.fy2ndsem
    usergrade2 = request.user.sy1stsem
    usergrade3 = request.user.sy2ndsem
    usergrade4 = request.user.sysummer
    usergrade5 = request.user.ty1stsem
    usergrade6 = request.user.ty2ndsem
    usergrade7 = request.user.fy1stsem
    usergrade8 = request.user.fry2ndsem
    context = {'userprof': userprof, 'usergrade': usergrade, 'usergrade1': usergrade1, 'usergrade2': usergrade2, 'usergrade3': usergrade3, 'usergrade4': usergrade4, 'usergrade5': usergrade5, 'usergrade6': usergrade6, 'usergrade7': usergrade7, 'usergrade8': usergrade8,}
    return render(request, 'accounts/StudentProfile.html' , context)

@login_required(login_url='loginPage')
@student_only
def studadvise(request):
    userprof1 = request.user.studentprof
    
    if( userprof1.user_yrandsec == '101' ):
         usergrade = request.user.studentgrades
         arr=[[113,usergrade.gned11], [115,usergrade.dcit21], [116,usergrade.dcit22]]    
         rows, cols = (3, 2)
         subj=[]
         for f in range(rows):
          subj.append(model.predict([arr[f]]))
         
         scndyrstnding = 2
         thirdyrstnding = 2
         
    if( userprof1.user_yrandsec == '102' ):
         usergrade = request.user.fy2ndsem
         usergrade1 = request.user.studentgrades
         arr=[[126,usergrade.dcit23],[132,usergrade1.gned11]]    
         rows, cols = (2, 2)
         subj=[]
         for f in range(rows):
          subj.append(model.predict([arr[f]]))
         
         scndyrstnding = 2
         thirdyrstnding = 2



    if( userprof1.user_yrandsec == '201' or userprof1.user_yrandsec == '202'):
         usergrade = request.user.sy1stsem
         usergrade1 = request.user.studentgrades
         usergrade2 = request.user.fy2ndsem
         arr=[[216,usergrade.dcit24],[215,usergrade.itec55],[217,usergrade.dcit50],[113,usergrade1.gned11], [115,usergrade1.dcit21], [116,usergrade1.dcit22], [132,usergrade1.gned11], [126,usergrade2.dcit23]]    
         rows, cols = (8, 2)
         subj=[]
         for f in range(rows):
          subj.append(model.predict([arr[f]]))

         if (subj[0] == 'dcit55' and subj[1] == 'itec60' and subj[2] == 'dcit25,itec60' and subj[3] == 'gned12' and subj[4] == 'itec50' and subj[5] == 'dcit23' and subj[6] == 'gned14' and subj[7] == 'dcit24,dcit50,itec55'):
            scndyrstnding = 1
            thirdyrstnding = 2
         else:
            scndyrstnding = 2
            thirdyrstnding = 2
   

    if( userprof1.user_yrandsec == '202' ):
         usergrade = request.user.sy2ndsem
         arr=[[223,usergrade.itec60]]    
         rows, cols = (1, 2)
         subj=[]
         for f in range(rows):
          subj.append(model.predict([arr[f]]))

                   

    if( userprof1.user_yrandsec == '203' or userprof1.user_yrandsec == '302' or userprof1.user_yrandsec == '301' or userprof1.user_yrandsec == '401'):
         usergrade = request.user.sysummer
         usergrade1 = request.user.sy2ndsem
         usergrade2 = request.user.sy1stsem
         usergrade3 = request.user.studentgrades
         usergrade4 = request.user.fy2ndsem
         arr=[[232,usergrade1.itec60], [225,usergrade1.dcit55], [235,usergrade2.itec55],[216,usergrade2.dcit24],[215,usergrade2.itec55],[217,usergrade2.dcit50],[113,usergrade3.gned11], [115,usergrade3.dcit21], [116,usergrade3.dcit22], [132,usergrade3.gned11], [126,usergrade4.dcit23]]    
         rows, cols = (11, 2)
         subj=[]
         for f in range(rows):
          subj.append(model.predict([arr[f]]))


         if (subj[0] == 'itec85' and subj[1] == 'dcit26' and subj[2] == 'itec90' and subj[3] == 'dcit55' and subj[4] == 'itec60' and subj[5] == 'dcit25,itec60' and subj[6] == 'gned12' and subj[7] == 'itec50' and subj[8] == 'dcit23' and subj[9] == 'gned14' and subj[10] == 'dcit24,dcit50,itec55'):
            thirdyrstnding = 1
            scndyrstnding = 1
         else:
            thirdyrstnding = 2
            scndyrstnding = 1

    if( userprof1.user_yrandsec == '301' ):
         usergrade = request.user.ty1stsem
         usergrade1 = request.user.studentgrades
         usergrade2 = request.user.sysummer
         arr=[[311,usergrade.itec80], [312,usergrade.itec85], [313,usergrade.itec90], [315,usergrade.dcit26], [316,usergrade.dcit60], [231,usergrade2.stat2] ]    
         rows, cols = (6, 2)
         subj=[]
         for f in range(rows):
          subj.append(model.predict([arr[f]]))
         

    if( userprof1.user_yrandsec == '302' ):
         usergrade = request.user.ty2ndsem
         usergrade1 = request.user.sy2ndsem
         usergrade2 = request.user.sysummer
         arr=[[223,usergrade1.itec60], [232,usergrade2.itec75], [325,usergrade.itec100], [327,usergrade.itec200a]]    
         rows, cols = (4, 2)
         subj=[]
         for f in range(rows):
          subj.append(model.predict([arr[f]]))


    if( userprof1.user_yrandsec == '401' ):
         usergrade1 = request.user.ty1stsem
         usergrade = request.user.fy1stsem
         arr=[[312,usergrade1.itec85], [315,usergrade1.dcit26]]    
         rows, cols = (2, 2)
         subj=[]
         for f in range(rows):
          subj.append(model.predict([arr[f]]))

    

    if rows == 0:
     return redirect("home")
            


    print(subj)

    
    context = {'usergrade': usergrade, 'userprof': userprof1, 'subj':subj, 'scndyrstnding': scndyrstnding, 'thirdyrstnding': thirdyrstnding }
    return render(request, 'accounts/student advising.html', context )


def gradesupdate(request, pk):
     studgrade = studentgrades.objects.get(user__username=pk)
     studgrade1 = fy2ndsem.objects.get(user__username=pk)
     studgrade2 = sy1stsem.objects.get(user__username=pk)
     studgrade3 = sy2ndsem.objects.get(user__username=pk)
     studgrade4 = sysummer.objects.get(user__username=pk)
     studgrade5 = ty1stsem.objects.get(user__username=pk)
     studgrade6 = ty2ndsem.objects.get(user__username=pk)
     studgrade7 = fy1stsem.objects.get(user__username=pk)
     studgrade8 = fry2ndsem.objects.get(user__username=pk)
    
     if request.method == "POST":
        gned02 = request.POST['gned02']
        gned01 = request.POST['gned01']

        update_customer=studentgrades.objects.filter(user__username=pk).update(gned02=gned02)

        print("update query set: ",update_customer)

        context = {}
        return render(request, 'accounts/StudentInformation.html', {})



def viewstudents(request):
    adviserprof = request.user.adviserprof
    studentprofs = studentprof.objects.all()
    print(studentprofs)
   #context = {'studentprof': studentprofs, 'adviserprof':adviserprof  } 
   
    return render(request, 'accounts/ViewStudent.html', {'studentprofs': studentprofs, 'adviserprof': adviserprof })



def studentinfo(request, pk):
    studinfo = studentprof.objects.get(user__username=pk)
    studgrade = studentgrades.objects.get(user__username=pk)
    studgrade1 = fy2ndsem.objects.get(user__username=pk)
    studgrade2 = sy1stsem.objects.get(user__username=pk)
    studgrade3 = sy2ndsem.objects.get(user__username=pk)
    studgrade4 = sysummer.objects.get(user__username=pk)
    studgrade5 = ty1stsem.objects.get(user__username=pk)
    studgrade6 = ty2ndsem.objects.get(user__username=pk)
    studgrade7 = fy1stsem.objects.get(user__username=pk)
    studgrade8 = fry2ndsem.objects.get(user__username=pk)

    if request.method == "POST":
        gned02 = request.POST['gned02']
        gned05 = request.POST['gned05']
        gned11 = request.POST['gned11']
        cosc50 = request.POST['cosc50'] 
        dcit21 = request.POST['dcit21']
        dcit22 = request.POST['dcit22']
        fitt1 = request.POST['fitt1']
        nstp1 = request.POST['nstp1']
        ornt1 = request.POST['ornt1']
        #first year 2nd sem
        gned01 = request.POST['gned01']
        gned06 = request.POST['gned06']
        gned12 = request.POST['gned12']
        gned03 = request.POST['gned03']
        itec50 = request.POST['itec50']
        dcit23 = request.POST['dcit23']
        fitt2 = request.POST['fitt2']
        nstp2 = request.POST['nstp2']
        #second year 1st sem
        gned04 = request.POST['gned04']
        gned07 = request.POST['gned07']
        gned10 = request.POST['gned10']
        gned14 = request.POST['gned14']
        itec55 = request.POST['itec55']
        dcit24 = request.POST['dcit24']
        dcit50 = request.POST['dcit50']
        fitt3 = request.POST['fitt3']
        #second year 2nd sem
        gned08 = request.POST['gned08']
        dcit25 = request.POST['dcit25']
        itec60 = request.POST['itec60']
        itec65 = request.POST['itec65']
        dcit55 = request.POST['dcit55']
        itec70 = request.POST['itec70']
        fitt4 = request.POST['fitt4']
        #second year summer
        stat2 = request.POST['stat2']
        itec75 = request.POST['itec75']
        #third year 1st sem
        itec80 = request.POST['itec80']
        itec85 = request.POST['itec85']
        itec90 = request.POST['itec90']
        insy55 = request.POST['insy55']
        dcit26 = request.POST['dcit26']
        dcit60 = request.POST['dcit60']
        #third year 2nd sem
        gned09 = request.POST['gned09']
        itec95 = request.POST['itec95']
        itec101 = request.POST['itec101']
        itec106 = request.POST['itec106']
        itec100 = request.POST['itec100']
        itec105 = request.POST['itec105']
        itec200a = request.POST['itec200a']
        #fourth year 1st sem
        dcit65 = request.POST['dcit65']
        itec111 = request.POST['itec111']
        itec116 = request.POST['itec116']
        itec110 = request.POST['itec110']
        itec200b = request.POST['itec200b']
        #fourth year 2nd sem
        itec199 = request.POST['itec199']


        studentgrades.objects.filter(user__username=pk).update(gned02=gned02,gned05=gned05,gned11=gned11,cosc50=cosc50,dcit21=dcit21,dcit22=dcit22,fitt1=fitt1,nstp1=nstp1,ornt1=ornt1)
        fy2ndsem.objects.filter(user__username=pk).update(gned01=gned01,gned06=gned06,gned12=gned12,gned03=gned03,itec50=itec50,dcit23=dcit23,fitt2=fitt2,nstp2=nstp2)
        sy1stsem.objects.filter(user__username=pk).update(gned04=gned04,gned07=gned07,gned10=gned10,gned14=gned14,itec55=itec55,dcit24=dcit24,dcit50=dcit50,fitt3=fitt3)
        sy2ndsem.objects.filter(user__username=pk).update(gned08=gned08,dcit25=dcit25,itec60=itec60,itec65=itec65,dcit55=dcit55,itec70=itec70,fitt4=fitt4)
        sysummer.objects.filter(user__username=pk).update(stat2=stat2,itec75=itec75)
        ty1stsem.objects.filter(user__username=pk).update(itec80=itec80,itec85=itec85,itec90=itec90,insy55=insy55,dcit26=dcit26,dcit60=dcit60)
        ty2ndsem.objects.filter(user__username=pk).update(gned09=gned09,itec95=itec95,itec101=itec101,itec106=itec106,itec100=itec100,itec105=itec105,itec200a=itec200a)
        fy1stsem.objects.filter(user__username=pk).update(dcit65=dcit65,itec111=itec111,itec116=itec116,itec110=itec110,itec200b=itec200b)
        fry2ndsem.objects.filter(user__username=pk).update(itec199=itec199)
        
    context = {'studinfo': studinfo,'studgrade': studgrade, 'studgrade1': studgrade1, 'studgrade2': studgrade2, 'studgrade3': studgrade3, 'studgrade4': studgrade4, 'studgrade5': studgrade5, 'studgrade6': studgrade6, 'studgrade7': studgrade7, 'studgrade8': studgrade8 }
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
   
            messages.success(request, "Account successfuly created for "+ username)
            return redirect("loginPage")



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


def checklist(request):
    return render(request, 'accounts/checklist.html')

#@login_required(login_url='loginPage')
#def adminPage(request):
#    return render(request, 'http://127.0.0.1:8000/admin/')    

#def loginstud(request, pk_test):
 #   studentprof1 = studentprof.objects.get(user_id=pk_test)
  #  context = {'studentprof':studentprof1, }
   # return render(request, 'accounts/StudentProfile.html', context)