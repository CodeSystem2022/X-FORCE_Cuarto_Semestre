# Generated by Django 4.2.5 on 2023-11-08 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_alter_mail_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default='key', max_length=50),
            preserve_default=False,
        ),
    ]
