# Generated by Django 3.1.6 on 2021-02-25 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210225_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='product',
            new_name='name',
        ),
    ]
