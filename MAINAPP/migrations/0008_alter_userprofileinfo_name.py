# Generated by Django 3.2.4 on 2021-06-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0007_userprofileinfo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
