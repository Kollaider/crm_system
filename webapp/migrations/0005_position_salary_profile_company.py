# Generated by Django 4.1.7 on 2023-02-20 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_profile_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.office'),
        ),
    ]
