# Generated by Django 3.1.4 on 2020-12-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
