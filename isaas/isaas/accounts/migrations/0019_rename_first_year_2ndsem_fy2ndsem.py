# Generated by Django 4.1.5 on 2023-01-11 02:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0018_rename_fy2ndsem_first_year_2ndsem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='First_Year_2ndSem',
            new_name='fy2ndsem',
        ),
    ]