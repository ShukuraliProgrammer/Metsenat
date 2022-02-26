# Generated by Django 4.0 on 2022-02-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_sponsormodel_choice_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsormodel',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('approved', 'approved'), ('moderation', 'moderation'), ('canceled', 'canceled')], max_length=100, null=True),
        ),
    ]
