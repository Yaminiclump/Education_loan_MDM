# Generated by Django 3.2 on 2022-01-05 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdm_services', '0002_pincode_search_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pincode',
            name='search_tag',
        ),
    ]
