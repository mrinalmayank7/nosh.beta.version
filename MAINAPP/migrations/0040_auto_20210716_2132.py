# Generated by Django 3.2.4 on 2021-07-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0039_auto_20210716_1922'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Workshop_Enrollment',
            new_name='WorkshopEnrollment',
        ),
        migrations.AlterField(
            model_name='workshop',
            name='workshop_end_paragraph_heading',
            field=models.CharField(blank=True, help_text='Appers at the end', max_length=300),
        ),
    ]
