# Generated by Django 4.2 on 2023-05-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_orderhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='sign',
            field=models.CharField(max_length=400, verbose_name='Signature'),
        ),
    ]
