# Generated by Django 4.1.7 on 2023-02-20 20:54

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_profile_office_position_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
