# Generated by Django 2.0 on 2019-12-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191210_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=0.0),
            preserve_default=False,
        ),
    ]
