# Generated by Django 4.1.5 on 2023-01-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_rename_adviser_course_adviserprof_adviser_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adviserprof',
            name='adviser_position',
            field=models.CharField(max_length=200, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='cosc50',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='dcit21',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='dcit22',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='fitt1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='gned02',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='gned05',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='gned11',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='nstp1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='ornt1',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
