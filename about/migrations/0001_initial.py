# Generated by Django 2.1.5 on 2020-03-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ABout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vission', models.TextField()),
                ('mission', models.TextField()),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
    ]
