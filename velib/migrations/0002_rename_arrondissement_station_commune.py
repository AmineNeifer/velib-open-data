# Generated by Django 4.0.2 on 2022-02-27 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('velib', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='arrondissement',
            new_name='commune',
        ),
    ]