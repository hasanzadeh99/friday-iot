# Generated by Django 4.0.5 on 2022-06-27 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friday', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeStation',
            new_name='HomeSide',
        ),
        migrations.RenameModel(
            old_name='ServerStation',
            new_name='ServerSide',
        ),
    ]
