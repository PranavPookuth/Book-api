# Generated by Django 5.1.1 on 2024-10-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0011_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
