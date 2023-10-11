# Generated by Django 4.2.5 on 2023-10-11 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_alter_category_name_alter_label_name_and_more'),
        ('ShoppingCart', '0002_product_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='Product.product'),
        ),
        migrations.DeleteModel(
            name='Product_Cart',
        ),
    ]
