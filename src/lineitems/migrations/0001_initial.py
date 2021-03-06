# Generated by Django 2.0 on 2020-02-11 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0014_product_timestamp'),
        ('carts', '0002_cart_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=120)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=120)),
                ('cart_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carts.Cart')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
        ),
    ]
