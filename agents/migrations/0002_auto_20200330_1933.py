# Generated by Django 2.1.5 on 2020-03-30 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agents',
            new_name='Agent',
        ),
    ]
