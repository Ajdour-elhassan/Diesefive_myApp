# Generated by Django 3.1.4 on 2020-12-16 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_auto_20201216_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sub_title',
        ),
    ]
