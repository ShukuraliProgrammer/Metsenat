# Generated by Django 4.0 on 2022-02-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsorshipmodel',
            options={'ordering': ['-created_date'], 'verbose_name': 'Sponsorship', 'verbose_name_plural': 'Sponsorships'},
        ),
        migrations.AlterField(
            model_name='sponsormodel',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sponsormodel',
            name='enter_money',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
