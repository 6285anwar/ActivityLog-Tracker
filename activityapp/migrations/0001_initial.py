# Generated by Django 4.0.6 on 2022-08-04 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, null=True)),
                ('email', models.EmailField(max_length=240, null=True)),
                ('username', models.CharField(max_length=240, null=True)),
                ('password', models.CharField(max_length=240, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='activitylog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.CharField(max_length=250, null=True)),
                ('typeofbusiness', models.CharField(max_length=250, null=True)),
                ('metpersonname', models.CharField(max_length=250, null=True)),
                ('designation', models.CharField(max_length=250, null=True)),
                ('phone', models.CharField(max_length=250, null=True)),
                ('stage', models.CharField(max_length=250, null=True)),
                ('location', models.CharField(max_length=250, null=True)),
                ('nextmeetingdate', models.DateField(blank=True, null=True)),
                ('remark', models.CharField(max_length=250, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='activityapp.user_registration')),
            ],
        ),
    ]
