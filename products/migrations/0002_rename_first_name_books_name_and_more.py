# Generated by Django 4.2.1 on 2023-06-17 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='last_name',
            new_name='price',
        ),
    ]
