# Generated by Django 4.0.6 on 2022-08-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('phoneNo', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
