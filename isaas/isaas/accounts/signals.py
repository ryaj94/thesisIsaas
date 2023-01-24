from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.models import Group

def create_profile(sender , instance, created, **kwargs):
    if created:
         group = Group.objects.get(name='forapproval')
         instance.groups.add(group)
         studentprof.objects.create(
            user=instance
            )
         studentgrades.objects.create(user=instance)
         fy2ndsem.objects.create(user=instance)
         sy1stsem.objects.create(user=instance)
         sy2ndsem.objects.create(user=instance)
         sysummer.objects.create(user=instance)
         ty1stsem.objects.create(user=instance)
         ty2ndsem.objects.create(user=instance)
         fy1stsem.objects.create(user=instance)
         fry2ndsem.objects.create(user=instance)

post_save.connect(create_profile, sender=User)