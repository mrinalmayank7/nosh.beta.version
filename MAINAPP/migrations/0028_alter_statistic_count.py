# Generated by Django 3.2.4 on 2021-06-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0027_auto_20210630_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='count',
            field=models.CharField(max_length=300),
        ),
    ]