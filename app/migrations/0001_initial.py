# Generated by Django 4.2.6 on 2023-11-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fac_id', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=150, unique=True)),
                ('email_id', models.EmailField(max_length=150, unique=True)),
            ],
        ),
    ]
