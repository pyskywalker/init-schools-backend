# Generated by Django 4.0.4 on 2022-05-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_contacts_location_remove_mainuser_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='permissions',
            field=models.ManyToManyField(related_name='rolePermission', to='Users.permissions'),
        ),
    ]
