from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class studentprof(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    user_fname = models.CharField(max_length=200, verbose_name='First Name')
    user_mname = models.CharField(max_length=200, verbose_name='Middle Name')
    user_lname = models.CharField(max_length=200, verbose_name='Last Name')
    user_course = models.CharField(max_length=200, verbose_name='Course')
    user_yrandsec = models.CharField(max_length=200, verbose_name='Year')
    user_section = models.CharField(max_length=200, verbose_name='Section', null=True)
    user_address = models.CharField(max_length=200, verbose_name='Address')
    user_cnumber = models.CharField(max_length=200, verbose_name='Contact Number')

    def __str__(self):
        return f'{self.user_fname} {self.user_mname} {self.user_lname}'


class adviserprof(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    adviser_fname = models.CharField(max_length=200, verbose_name='First Name')
    adviser_mname = models.CharField(max_length=200, verbose_name='Middle Name')
    adviser_lname = models.CharField(max_length=200, verbose_name='Last Name')
    adviser_position = models.CharField(max_length=200, verbose_name='Position') 
    adviser_address = models.CharField(max_length=200, verbose_name='Address')
    adviser_cnumber = models.CharField(max_length=200, verbose_name='Contact Number')

    def __str__(self):
        return f'{self.adviser_fname} {self.adviser_mname} {self.adviser_lname}'


class studentgrades(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    gned02 = models.FloatField(null=True)
    gned05 = models.FloatField(null=True)
    gned11 = models.FloatField(null=True)
    cosc50 = models.FloatField(null=True)
    dcit21 = models.FloatField(null=True)
    dcit22 = models.FloatField(null=True)
    fitt1 = models.FloatField(null=True)
    nstp1 = models.FloatField(null=True)
    ornt1 = models.FloatField(null=True)
    
    def __str__(self):
        return str(self.user)

class fy2ndsem(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    gned01 = models.FloatField(null=True)
    gned06 = models.FloatField(null=True)
    gned12 = models.FloatField(null=True)
    gned03 = models.FloatField(null=True)
    itec50 = models.FloatField(null=True)
    dcit23 = models.FloatField(null=True)
    fitt2 = models.FloatField(null=True)
    nstp2 = models.FloatField(null=True)

    def __str__(self):
        return str(self.user)

class sy1stsem(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    gned04 = models.FloatField(null=True)
    gned07 = models.FloatField(null=True)
    gned10 = models.FloatField(null=True)
    gned14 = models.FloatField(null=True)
    itec55 = models.FloatField(null=True)
    dcit24 = models.FloatField(null=True)
    dcit50 = models.FloatField(null=True)
    fitt3 = models.FloatField(null=True)
    
    def __str__(self):
        return str(self.user)

class sy2ndsem(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    gned08 = models.FloatField(null=True)
    dcit25 = models.FloatField(null=True)
    itec60 = models.FloatField(null=True)
    itec65 = models.FloatField(null=True)
    dcit55 = models.FloatField(null=True)
    itec70 = models.FloatField(null=True)
    fitt4 = models.FloatField(null=True)
    
    def __str__(self):
        return str(self.user)


class sysummer(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    stat2 = models.FloatField(null=True)
    itec75 = models.FloatField(null=True)
    
    def __str__(self):
        return str(self.user)
    
class ty1stsem(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    itec80 = models.FloatField(null=True)
    itec85 = models.FloatField(null=True)
    itec90 = models.FloatField(null=True)
    insy55 = models.FloatField(null=True)
    dcit26 = models.FloatField(null=True)
    dcit60 = models.FloatField(null=True)
    
    def __str__(self):
        return str(self.user)

class ty2ndsem(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    gned09 = models.FloatField(null=True)
    itec95 = models.FloatField(null=True)
    itec101 = models.FloatField(null=True)
    itec106 = models.FloatField(null=True)
    itec100 = models.FloatField(null=True)
    itec105 = models.FloatField(null=True)
    itec200a = models.FloatField(null=True)
    
    def __str__(self):
        return str(self.user)

class fy1stsem(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    dcit65 = models.FloatField(null=True)
    itec111 = models.FloatField(null=True)
    itec116 = models.FloatField(null=True)
    itec110 = models.FloatField(null=True)
    itec200b = models.FloatField(null=True)
    
    def __str__(self):
        return str(self.user)


class fry2ndsem(models.Model):
    user = models.OneToOneField(User, null=True , on_delete=models.CASCADE)
    itec199 = models.FloatField(null=True)
    
    def __str__(self):
        return str(self.user)
