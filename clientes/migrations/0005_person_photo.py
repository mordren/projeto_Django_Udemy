# Generated by Django 4.1.2 on 2022-10-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_person_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos'),
        ),
    ]
