# Generated by Django 4.0.4 on 2022-05-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0012_location_district_location_village_location_ward_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='village',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='ward',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]