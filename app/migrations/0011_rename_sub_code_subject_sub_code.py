# Generated by Django 4.2.6 on 2023-11-22 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_faculty_tcp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='Sub_code',
            new_name='sub_code',
        ),
    ]
