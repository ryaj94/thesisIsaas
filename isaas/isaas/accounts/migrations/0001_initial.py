# Generated by Django 4.1.5 on 2023-01-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Student ID')),
                ('user_fname', models.CharField(max_length=200, verbose_name='First Name')),
                ('user_mname', models.CharField(max_length=200, verbose_name='Middle Name')),
                ('user_lname', models.CharField(max_length=200, verbose_name='Last Name')),
                ('user_course', models.CharField(max_length=200, verbose_name='Course')),
                ('user_yrandsec', models.CharField(max_length=200, verbose_name='Year and Section')),
                ('user_address', models.CharField(max_length=200, verbose_name='Address')),
                ('user_cnumber', models.CharField(max_length=200, verbose_name='Contact Number')),
                ('user_emailadd', models.CharField(max_length=200, verbose_name='E-mail Address')),
                ('user_password', models.CharField(max_length=200, verbose_name='Password')),
            ],
        ),
    ]