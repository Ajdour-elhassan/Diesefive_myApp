# Generated by Django 3.1.4 on 2020-12-05 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20201205_1849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('title',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]
