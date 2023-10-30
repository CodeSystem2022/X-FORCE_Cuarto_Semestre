# Generated by Django 4.2.5 on 2023-10-11 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchases', '0011_alter_purchaseproduct_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='purchaseproduct',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]