# Generated by Django 3.1.4 on 2020-12-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_auto_20201208_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.CharField(choices=[('Sanjay', 'Sanjay')], max_length=200, null=True),
        ),
    ]
