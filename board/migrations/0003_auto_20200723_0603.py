# Generated by Django 3.0.8 on 2020-07-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200723_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='img',
            field=models.ImageField(blank=True, upload_to='./ans_img/'),
        ),
    ]