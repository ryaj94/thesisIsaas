# Generated by Django 4.1.5 on 2023-01-11 02:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0017_studentprof_user_section_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='fy2ndsem',
            new_name='First_Year_2ndSem',
        ),
    ]
