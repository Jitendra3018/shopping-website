# Generated by Django 2.2.24 on 2021-12-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_shop', '0002_auto_20211223_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='product_image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='carted',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
