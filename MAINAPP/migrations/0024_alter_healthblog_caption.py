# Generated by Django 3.2.4 on 2021-06-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0023_auto_20210627_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthblog',
            name='caption',
            field=models.CharField(blank=True, help_text='Please add min 45 and max 55 (count space as well)characters to adjust it in flip card size', max_length=500),
        ),
    ]