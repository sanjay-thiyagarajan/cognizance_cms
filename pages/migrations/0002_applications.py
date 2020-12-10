# Generated by Django 3.1.4 on 2020-12-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, null=True)),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('CSE(AI)', 'CSE(AI)'), ('CYS', 'CYS'), ('CCE', 'CCE'), ('ECE', 'ECE')], max_length=100, null=True)),
                ('domain', models.CharField(choices=[('Cyber Security', 'Cyber Security'), ('AI', 'AI'), ('Data Science', 'Data Science'), ('Competitive Programming', 'Competitive Programming'), ('Hackathons', 'Hackathons'), ('Open Source', 'Open Source')], max_length=100, null=True)),
                ('ques1', models.TextField(max_length=400, null=True)),
                ('writeup', models.TextField(max_length=1000, null=True)),
                ('ac_year', models.CharField(choices=[('I year', 'I year'), ('II year', 'II year'), ('III year', 'III year'), ('IV year', 'IV year')], max_length=20, null=True)),
                ('applied_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Under review', 'Under review'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=50, null=True)),
                ('experience', models.TextField(max_length=500, null=True)),
                ('reviewer', models.CharField(choices=[('Sanjay', 'Sanjay')], max_length=100, null=True)),
            ],
        ),
    ]
