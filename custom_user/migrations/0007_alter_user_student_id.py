# Generated by Django 5.0.4 on 2024-06-04 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0006_rename_student_user_student_id'),
        ('studentLife_system', '0010_accreditation_adminlogin_adviser_financialstatement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentLife_system.studentinfo'),
        ),
    ]
