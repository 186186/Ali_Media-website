# Generated by Django 3.0.7 on 2020-07-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_auto_20200721_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='static\\image\\'),
        ),
    ]
