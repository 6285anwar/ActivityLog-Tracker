# Generated by Django 4.0.6 on 2022-08-07 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityapp', '0006_alter_activitylog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
