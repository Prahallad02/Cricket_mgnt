# Generated by Django 5.0.6 on 2024-06-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cric_Mgnt', '0002_playersmodel_coached_by_alter_coachmodel_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersmodel',
            name='matches_played',
            field=models.IntegerField(default=0),
        ),
    ]