# Generated by Django 4.2.6 on 2023-11-21 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_semester_sem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='reg_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_year', to='app.semester'),
        ),
    ]
