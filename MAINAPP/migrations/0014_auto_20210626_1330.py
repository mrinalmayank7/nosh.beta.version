# Generated by Django 3.2.4 on 2021-06-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0013_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='caption',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
