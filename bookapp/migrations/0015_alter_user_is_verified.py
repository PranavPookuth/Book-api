# Generated by Django 5.1.1 on 2024-10-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0014_alter_user_options_remove_user_address1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]