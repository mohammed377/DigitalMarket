# Generated by Django 4.2.1 on 2023-05-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
