# Generated by Django 4.2.6 on 2023-10-30 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='createdTime',
        ),
    ]
