# Generated by Django 4.2.1 on 2023-05-30 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_userprofile_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
    ]