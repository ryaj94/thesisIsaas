# Generated by Django 4.1.5 on 2023-01-17 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_adviserprof_adviser_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fry2ndsem',
            name='itec199',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy1stsem',
            name='dcit65',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy1stsem',
            name='itec110',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy1stsem',
            name='itec111',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy1stsem',
            name='itec116',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy1stsem',
            name='itec200b',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy2ndsem',
            name='dcit23',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy2ndsem',
            name='fitt2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy2ndsem',
            name='gned01',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy2ndsem',
            name='gned03',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy2ndsem',
            name='gned06',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy2ndsem',
            name='gned12',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy2ndsem',
            name='itec50',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fy2ndsem',
            name='nstp2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprof',
            name='user_address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='studentprof',
            name='user_cnumber',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='studentprof',
            name='user_course',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='studentprof',
            name='user_fname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='studentprof',
            name='user_lname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='studentprof',
            name='user_mname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='studentprof',
            name='user_section',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='studentprof',
            name='user_yrandsec',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='sy1stsem',
            name='dcit24',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy1stsem',
            name='dcit50',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy1stsem',
            name='fitt3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy1stsem',
            name='gned04',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy1stsem',
            name='gned07',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy1stsem',
            name='gned10',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy1stsem',
            name='gned14',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy1stsem',
            name='itec55',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy2ndsem',
            name='dcit25',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy2ndsem',
            name='dcit55',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy2ndsem',
            name='fitt4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy2ndsem',
            name='gned08',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy2ndsem',
            name='itec60',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy2ndsem',
            name='itec65',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sy2ndsem',
            name='itec70',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sysummer',
            name='itec75',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sysummer',
            name='stat2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty1stsem',
            name='dcit26',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty1stsem',
            name='dcit60',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty1stsem',
            name='insy55',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty1stsem',
            name='itec80',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty1stsem',
            name='itec85',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty1stsem',
            name='itec90',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty2ndsem',
            name='gned09',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty2ndsem',
            name='itec100',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty2ndsem',
            name='itec101',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty2ndsem',
            name='itec105',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty2ndsem',
            name='itec106',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty2ndsem',
            name='itec200a',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ty2ndsem',
            name='itec95',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
