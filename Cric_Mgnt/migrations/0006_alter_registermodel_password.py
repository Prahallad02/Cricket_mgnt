# Generated by Django 5.0 on 2024-06-17 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cric_Mgnt', '0005_loginmodel_registermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
