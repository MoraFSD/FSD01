# Generated by Django 5.1.4 on 2024-12-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_office', '0003_rename_sells_sell_rename_sell_items_sell_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='shop_id',
        ),
        migrations.AddField(
            model_name='sell_item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='название'),
        ),
    ]
