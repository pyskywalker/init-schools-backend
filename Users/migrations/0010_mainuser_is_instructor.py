# Generated by Django 4.0.4 on 2022-05-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_rename_permissions_userrole_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='is_instructor',
            field=models.BooleanField(default=False),
        ),
    ]
