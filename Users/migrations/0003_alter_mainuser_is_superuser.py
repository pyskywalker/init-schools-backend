# Generated by Django 4.0.4 on 2022-05-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_mainuser_age_alter_mainuser_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]