# Generated by Django 4.0 on 2022-02-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_sponsormodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsormodel',
            name='pay_type',
            field=models.CharField(choices=[('cash', 'cash'), ('card', 'card'), ('salary', 'salary')], max_length=100, null=True),
        ),
    ]
