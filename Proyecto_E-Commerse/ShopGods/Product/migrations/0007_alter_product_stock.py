# Generated by Django 4.2.5 on 2023-11-07 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]