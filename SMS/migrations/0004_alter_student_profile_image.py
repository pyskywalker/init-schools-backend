# Generated by Django 4.0.4 on 2022-05-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0003_alter_student_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(upload_to='students/<django.db.models.fields.CharField>/profile_image'),
        ),
    ]
