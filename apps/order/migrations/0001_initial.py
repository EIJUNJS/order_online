# Generated by Django 4.1.3 on 2022-11-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Upload time')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete')),
                ('count', models.IntegerField(default=1, verbose_name='goods amount')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('comment', models.CharField(default='', max_length=256, verbose_name='comment')),
            ],
            options={
                'verbose_name': 'Order goods',
                'verbose_name_plural': 'Order goods',
                'db_table': 'df_order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Upload time')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete')),
                ('order_id', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='Order id')),
                ('pay_method', models.SmallIntegerField(choices=[(1, 'cash on delivery'), (2, 'Wechat'), (3, 'Alipay'), (4, 'card payment')], default=3, verbose_name='Pay Method')),
                ('total_count', models.IntegerField(default=1, verbose_name='goods amount')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='SubTotal')),
                ('transit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Delivery Fee')),
                ('order_status', models.SmallIntegerField(choices=[(1, 'Pending Payment'), (2, 'to be delivered'), (3, 'Shipped'), (4, 'comment'), (5, 'Complete')], default=1, verbose_name='Status')),
                ('trade_no', models.CharField(default='', max_length=128, verbose_name='pay number')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
                'db_table': 'df_order_info',
            },
        ),
    ]