# Generated by Django 3.2.7 on 2021-10-11 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='user',
            new_name='client',
        ),
    ]
