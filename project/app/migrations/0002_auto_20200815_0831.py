# Generated by Django 3.1 on 2020-08-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]