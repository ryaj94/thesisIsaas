from django.urls import path
from . import views

urlpatterns = [
   path('registeruser/',views.registeruser, name="register"),
   path('',views.loginPage, name="loginPage"),
   path('logout',views.logoutUser, name="logout"),
   path('home',views.home, name="home"),
   path('sampleInput',views.sampleInput, name='sampleInput'),
   path('predict',views.predict, name='predict'),
   path('studadvise',views.studadvise, name="studadvise"),
   path('adviserprofile',views.adviserpro2, name="adviserprof"),
   path('viewstudents',views.viewstudents, name='viewstudent'),
   path('studentinfo/<str:pk>/',views.studentinfo, name='studentinfo'),
   path('gradesupdate/<str:pk>/',views.gradesupdate, name='gradesupdate'),
   path('checklist',views.checklist , name='checklist')
 #  path('loginstud/<str:pk_test>/', views.loginstud, name="loginstud")
   

]
