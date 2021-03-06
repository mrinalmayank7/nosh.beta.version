# Generated by Django 3.2.4 on 2021-07-14 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0036_auto_20210714_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='participants',
        ),
        migrations.AddField(
            model_name='workshop_enrollment',
            name='participant_email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workshop',
            name='workshop_name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='workshop_enrollment',
            name='participant_name',
            field=models.CharField(max_length=300),
        ),
    ]
