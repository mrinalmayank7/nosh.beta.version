# Generated by Django 3.2.4 on 2021-07-16 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0038_auto_20210715_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workshop',
            old_name='sub_body3',
            new_name='workshop_end_paragraph_body',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='sub_heading3',
        ),
        migrations.AddField(
            model_name='workshop',
            name='workshop_end_paragraph_heading',
            field=models.CharField(blank=True, help_text='Appers at the end white box', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_colors_available',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_sub_heading',
            field=models.CharField(blank=True, help_text='If you have a detailed description of product with sub heading add here', max_length=300),
        ),
        migrations.AlterField(
            model_name='workshop_enrollment',
            name='enrolled_on',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
