# Generated by Django 4.2.5 on 2023-11-07 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
    ]
