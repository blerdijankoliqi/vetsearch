# Generated by Django 4.0.10 on 2023-02-15 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_subpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localitypage',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='localitypage',
            name='meta_title',
        ),
    ]