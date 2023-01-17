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

    def __str__(self):
        return f'{self.adviser_fname} {self.adviser_mname} {self.adviser_lname}'


class studentgrades(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    gned02 = models.FloatField(null=True , blank=True)
    gned05 = models.FloatField(null=True , blank=True)
    gned11 = models.FloatField(null=True , blank=True)
    cosc50 = models.FloatField(null=True , blank=True)
    dcit21 = models.FloatField(null=True , blank=True)
    dcit22 = models.FloatField(null=True , blank=True)
    fitt1 = models.FloatField(null=True , blank=True)
    nstp1 = models.FloatField(null=True , blank=True)
    ornt1 = models.FloatField(null=True , blank=True)
    
    def __str__(self):
        return str(self.user)

class fy2ndsem(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    gned01 = models.FloatField(null=True , blank=True)
    gned06 = models.FloatField(null=True , blank=True)
    gned12 = models.FloatField(null=True , blank=True)
    gned03 = models.FloatField(null=True , blank=True)
    itec50 = models.FloatField(null=True , blank=True)
    dcit23 = models.FloatField(null=True , blank=True)
    fitt2 = models.FloatField(null=True , blank=True)
    nstp2 = models.FloatField(null=True , blank=True)

    def __str__(self):
        return str(self.user)

class sy1stsem(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    gned04 = models.FloatField(null=True , blank=True)
    gned07 = models.FloatField(null=True , blank=True)
    gned10 = models.FloatField(null=True , blank=True)
    gned14 = models.FloatField(null=True , blank=True)
    itec55 = models.FloatField(null=True , blank=True)
    dcit24 = models.FloatField(null=True , blank=True)
    dcit50 = models.FloatField(null=True , blank=True)
    fitt3 = models.FloatField(null=True , blank=True)
    
    def __str__(self):
        return str(self.user)

class sy2ndsem(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    gned08 = models.FloatField(null=True , blank=True)
    dcit25 = models.FloatField(null=True , blank=True)
    itec60 = models.FloatField(null=True , blank=True)
    itec65 = models.FloatField(null=True , blank=True)
    dcit55 = models.FloatField(null=True , blank=True)
    itec70 = models.FloatField(null=True , blank=True)
    fitt4 = models.FloatField(null=True , blank=True)
    
    def __str__(self):
        return str(self.user)


class sysummer(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    stat2 = models.FloatField(null=True , blank=True)
    itec75 = models.FloatField(null=True , blank=True)
    
    def __str__(self):
        return str(self.user)
    
class ty1stsem(models.Model):
    user = models.OneToOneField(User, null=True , blank=True , on_delete=models.CASCADE)
    itec80 = models.FloatField(null=True , blank=True)
    itec85 = models.FloatField(null=True , blank=True)
    itec90 = models.FloatField(null=True , blank=True)
    insy55 = models.FloatField(null=True , blank=True)
    dcit26 = models.FloatField(null=True , blank=True)
    dcit60 = models.FloatField(null=True , blank=True)
    
    def __str__(self):
        return str(self.user)

class ty2ndsem(models.Model):
    user = models.OneToOneField(User, null=True ,blank=True , on_delete=models.CASCADE)
    gned09 = models.FloatField(null=True , blank=True)
    itec95 = models.FloatField(null=True , blank=True)
    itec101 = models.FloatField(null=True , blank=True)
    itec106 = models.FloatField(null=True , blank=True)
    itec100 = models.FloatField(null=True , blank=True)
    itec105 = models.FloatField(null=True , blank=True)
    itec200a = models.FloatField(null=True , blank=True)
    
    def __str__(self):
        return str(self.user)

class fy1stsem(models.Model):
    user = models.OneToOneField(User, null=True ,blank=True , on_delete=models.CASCADE)
    dcit65 = models.FloatField(null=True , blank=True)
    itec111 = models.FloatField(null=True , blank=True)
    itec116 = models.FloatField(null=True , blank=True)
    itec110 = models.FloatField(null=True , blank=True)
    itec200b = models.FloatField(null=True , blank=True)
    
    def __str__(self):
        return str(self.user)


class fry2ndsem(models.Model):
    user = models.OneToOneField(User, null=True ,blank=True , on_delete=models.CASCADE)
    itec199 = models.FloatField(null=True , blank=True)
    
    def __str__(self):
        return str(self.user)



