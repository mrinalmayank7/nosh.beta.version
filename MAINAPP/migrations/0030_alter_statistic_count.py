# Generated by Django 3.2.4 on 2021-06-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0029_alter_statistic_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='count',
            field=models.CharField(max_length=300),
        ),
    ]
