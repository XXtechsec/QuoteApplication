# Generated by Django 2.1 on 2019-07-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotes', '0006_auto_20190715_1806'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AlterField(
            model_name='quote',
            name='Services',
            field=models.ManyToManyField(to='Quotes.ProductsCommerxcatalogProducts'),
        ),
    ]