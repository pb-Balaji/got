# Generated by Django 4.1.5 on 2023-01-21 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='messege',
            new_name='message',
        ),
    ]