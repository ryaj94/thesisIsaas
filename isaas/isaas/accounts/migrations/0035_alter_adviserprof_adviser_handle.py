# Generated by Django 4.1.5 on 2023-01-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_adviserprof_adviser_handle_alter_fry2ndsem_itec199_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adviserprof',
            name='adviser_handle',
            field=models.IntegerField(blank=True, null=True, verbose_name='School Year Handle'),
        ),
    ]
