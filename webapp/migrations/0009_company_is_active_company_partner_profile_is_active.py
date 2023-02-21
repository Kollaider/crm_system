# Generated by Django 4.1.7 on 2023-02-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0008_company_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="company",
            name="partner",
            field=models.ManyToManyField(blank=True, to="webapp.company"),
        ),
        migrations.AddField(
            model_name="profile",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]