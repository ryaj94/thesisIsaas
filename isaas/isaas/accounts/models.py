from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class studentprof(models.Model):
    user = models.OneToOneField(User, null=True, blank=True , on_delete=models.CASCADE)
    user_fname = models.CharField(max_length=200, verbose_name='First Name' , blank=True , null=True)
    user_mname = models.CharField(max_length=200, verbose_name='Middle Name' , blank=True , null=True)
    user_lname = models.CharField(max_length=200, verbose_name='Last Name' , blank=True , null=True)
    user_course = models.CharField(max_length=200, verbose_name='Course' , blank=True , null=True)
    user_yrandsec = models.CharField(max_length=200, verbose_name='Year' , blank=True , null=True)
    user_section = models.CharField(max_length=200, verbose_name='Section', blank=True , null=True)
    user_address = models.CharField(max_length=200, verbose_name='Address' , blank=True , null=True)
    user_cnumber = models.CharField(max_length=200, verbose_name='Contact Number' , blank=True , null=True)

    def __str__(self):
        return f'{self.user_fname} {self.user_mname} {self.user_lname}'


class adviserprof(models.Model):
    user = models.OneToOneField(User, null=True, blank=True  , on_delete=models.CASCADE)
    adviser_fname = models.CharField(max_length=200, verbose_name='First Name' , null=True, blank=True )
    adviser_mname = models.CharField(max_length=200, verbose_name='Middle Name' , null=True, blank=True )
    adviser_lname = models.CharField(max_length=200, verbose_name='Last Name' , null=True, blank=True )
    adviser_position = models.CharField(max_length=200, verbose_name='Position' , null=True, blank=True ) 
    adviser_address = models.CharField(max_length=200, verbose_name='Address' , null=True, blank=True )
    adviser_cnumber = models.CharField(max_length=200, verbose_name='Contact Number' , null=True, blank=True )
    adviser_handle = models.IntegerField( verbose_name='School Year Handle' , null=True, blank=True )

    def __str__(self):
        return f'{self.adviser_fname} {self.adviser_mname} {self.adviser_lname}'


class studentgrades(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    gned02 = models.CharField(max_length=200, null=True , blank=True ,default = 'Not yet taken')
    gned05 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    gned11 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    cosc50 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    dcit21 = models.CharField(max_length=200, null=True , blank=True ,default = 'Not yet taken')
    dcit22 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    fitt1 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    nstp1 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    ornt1 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    
    def __str__(self):
        return str(self.user)

class fy2ndsem(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    gned01 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    gned06 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    gned12 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    gned03 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec50 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    dcit23 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    fitt2 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    nstp2 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')

    def __str__(self):
        return str(self.user)

class sy1stsem(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    gned04 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    gned07 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    gned10 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    gned14 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec55 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    dcit24 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    dcit50 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    fitt3 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    
    def __str__(self):
        return str(self.user)

class sy2ndsem(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    gned08 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    dcit25 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec60 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec65 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    dcit55 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec70 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    fitt4 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    
    def __str__(self):
        return str(self.user)


class sysummer(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    stat2 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec75 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    
    def __str__(self):
        return str(self.user)
    
class ty1stsem(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    itec80 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec85 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec90 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    insy55 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    dcit26 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    dcit60 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    
    def __str__(self):
        return str(self.user)

class ty2ndsem(models.Model):
    user = models.OneToOneField(User, null=True ,blank=True , on_delete=models.CASCADE)
    gned09 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec95 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec101 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec106 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec100 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec105 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec200a = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    
    def __str__(self):
        return str(self.user)

class fy1stsem(models.Model):
    user = models.OneToOneField(User, null=True ,blank=True , on_delete=models.CASCADE)
    dcit65 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec111 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec116 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec110 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    itec200b = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    
    def __str__(self):
        return str(self.user)


class fry2ndsem(models.Model):
    user = models.OneToOneField(User, null=True ,blank=True , on_delete=models.CASCADE)
    itec199 = models.CharField(max_length=200,null=True , blank=True ,default = 'Not yet taken')
    
    def __str__(self):
        return str(self.user)



