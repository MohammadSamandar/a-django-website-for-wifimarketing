# Generated by Django 4.1.3 on 2023-05-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_alter_subscriptionplan_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='price',
            field=models.DecimalField(decimal_places=6, max_digits=20, verbose_name='قیمت'),
        ),
    ]
