# Generated by Django 4.0.4 on 2022-05-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0008_alter_student_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(upload_to='students/profile_image/2022-05-11 10:46:10.869796'),
        ),
    ]