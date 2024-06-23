# Generated by Django 5.0.6 on 2024-06-16 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cric_Mgnt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersmodel',
            name='coached_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Cric_Mgnt.coachmodel'),
        ),
        migrations.AlterModelTable(
            name='coachmodel',
            table='cric_mgnt_coachmodel',
        ),
        migrations.AlterModelTable(
            name='playersmodel',
            table='cric_mgnt_playersmodel',
        ),
    ]