from django.db import models
from db.base_model import BaseModel


class OrderInfo(BaseModel):
    """Order model class"""
    PAY_METHOD_CHOICES = (
        (1, "cash on delivery"),
        (2, "Wechat"),
        (3, "Alipay"),
        (4, 'card payment')
    )

    ORDER_STATUS_CHOICES = (
        (1, 'Pending Payment'),
        (2, 'to be delivered'),
        (3, 'Shipped'),
        (4, 'comment'),
        (5, 'Complete')
    )

    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='Order id')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='User')
    addr = models.ForeignKey('user.Address', on_delete=models.CASCADE, verbose_name='Address')
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='Pay Method')
    total_count = models.IntegerField(default=1, verbose_name='goods amount')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='SubTotal')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Delivery Fee')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='Status')
    trade_no = models.CharField(max_length=128, default='', verbose_name='pay number')

    class Meta:
        db_table = 'df_order_info'
        verbose_name = 'Order'
        verbose_name_plural = verbose_name


class OrderGoods(BaseModel):
    """订单商品模型类"""
    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE, verbose_name='order')
    sku = models.ForeignKey('goods.GoodsSKU', on_delete=models.CASCADE, verbose_name='goods_SKU')
    count = models.IntegerField(default=1, verbose_name='goods amount')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')  # 总价格
    comment = models.CharField(max_length=256, default='', verbose_name='comment')

    class Meta:
        db_table = 'df_order_goods'
        verbose_name = 'Order goods'
        verbose_name_plural = verbose_name
