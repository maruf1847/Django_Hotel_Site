# Generated by Django 2.1.5 on 2020-03-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20200329_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=10),
        ),
    ]
