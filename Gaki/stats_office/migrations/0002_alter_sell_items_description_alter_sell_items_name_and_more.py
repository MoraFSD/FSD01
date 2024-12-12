# Generated by Django 5.1.4 on 2024-12-06 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_office', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_items',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='sell_items',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='sell_items',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='delivery_adress',
            field=models.CharField(max_length=150, null=True, verbose_name='адрес доставки'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='description',
            field=models.DateField(verbose_name='дата Рождения'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='inn_fiz',
            field=models.CharField(max_length=12, null=True, verbose_name='ИНН физ. лица'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='inn_ur',
            field=models.CharField(max_length=10, null=True, verbose_name='ИНН юр. лица'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='name',
            field=models.CharField(max_length=50, verbose_name='имя пользователя'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='password',
            field=models.CharField(max_length=50, verbose_name='имя пользователя'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='patronymic',
            field=models.CharField(max_length=50, null=True, verbose_name='отчетство'),
        ),
        migrations.CreateModel(
            name='shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='stats_office.user_data', verbose_name='владелец магазина')),
            ],
        ),
        migrations.CreateModel(
            name='sells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_date', models.DateField(verbose_name='дата покупки')),
                ('item_id', models.ForeignKey(on_delete=models.SET(0), to='stats_office.sell_items', verbose_name='товар')),
                ('user_id', models.ForeignKey(on_delete=models.SET(0), to='stats_office.user_data', verbose_name='покупатель')),
                ('shop_id', models.ForeignKey(on_delete=models.SET(0), to='stats_office.shops', verbose_name='магазин')),
            ],
        ),
        migrations.AlterField(
            model_name='sell_items',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats_office.shops', verbose_name='магазин'),
        ),
        migrations.DeleteModel(
            name='shop',
        ),
    ]
