# Generated by Django 3.2.4 on 2021-06-26 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0010_rename_attach_useremail_mail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='useremail',
            name='mail_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]