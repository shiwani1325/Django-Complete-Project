# Generated by Django 4.2.7 on 2023-12-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='fullname',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
