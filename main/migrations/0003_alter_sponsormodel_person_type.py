# Generated by Django 4.0 on 2022-02-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_sponsorshipmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsormodel',
            name='person_type',
            field=models.CharField(choices=[('legal', 'legal'), ('physical', 'physical')], max_length=100),
        ),
    ]
