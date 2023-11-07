# Generated by Django 4.2.5 on 2023-11-05 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Purchases', '0002_rename_product_purchases_products_and_more'),
        ('Product', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='key',
            name='puschases',
        ),
        migrations.RemoveField(
            model_name='mail',
            name='puschases',
        ),
        migrations.RemoveField(
            model_name='others',
            name='puschases',
        ),
        migrations.AddField(
            model_name='key',
            name='puschase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Purchases.purchases'),
        ),
        migrations.AddField(
            model_name='mail',
            name='puschase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Purchases.purchases'),
        ),
        migrations.AddField(
            model_name='others',
            name='puschase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Purchases.purchases'),
        ),
        migrations.AddField(
            model_name='product',
            name='pay',
            field=models.BooleanField(default=False),
        ),
    ]