# Generated by Django 4.0.4 on 2022-05-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0012_remove_subjects_course_course_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subjects',
            field=models.ManyToManyField(related_name='course_subjects', to='SMS.subjects'),
        ),
    ]
