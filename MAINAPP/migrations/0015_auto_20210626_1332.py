# Generated by Django 3.2.4 on 2021-06-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0014_auto_20210626_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='caption',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
