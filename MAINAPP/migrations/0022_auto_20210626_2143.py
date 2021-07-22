# Generated by Django 3.2.4 on 2021-06-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0021_auto_20210626_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Please add max 17 characters to adjust it in flip card size', max_length=200)),
                ('caption', models.CharField(blank=True, help_text='Please add min 32 and max 40 characters to adjust it in flip card size', max_length=200)),
                ('introduction', models.TextField(blank=True, help_text='this text will be visible in flip card back')),
                ('description', models.TextField(blank=True, help_text='this text will be visible  in read more')),
                ('conclusion', models.TextField(blank=True, help_text='this text will be visible in read more')),
                ('image', models.ImageField(blank=True, help_text='crop image as square before upload to adjust in the template', null=True, upload_to='')),
                ('add_to_home', models.BooleanField(blank=True, default=False, help_text='Yes will enable to display it on home page', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='HealthTip',
        ),
    ]
