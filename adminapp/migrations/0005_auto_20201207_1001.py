# Generated by Django 3.1.4 on 2020-12-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_member_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
