# Generated by Django 4.2.5 on 2023-11-05 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Purchases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchases',
            old_name='product',
            new_name='products',
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='card_data',
        ),
    ]