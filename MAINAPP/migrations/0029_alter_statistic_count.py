# Generated by Django 3.2.4 on 2021-06-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0028_alter_statistic_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='count',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
