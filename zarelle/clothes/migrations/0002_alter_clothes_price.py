# Generated by Django 5.1.2 on 2024-10-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
    ]
