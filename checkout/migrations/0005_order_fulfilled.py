# Generated by Django 4.0.2 on 2022-03-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_remove_order_grand_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='fulfilled',
            field=models.BooleanField(default=False),
        ),
    ]
