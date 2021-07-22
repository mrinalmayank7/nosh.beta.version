# Generated by Django 3.2.4 on 2021-06-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0008_alter_userprofileinfo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('attach', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
