from django.db import models

def status_validator(order_status):
    return order_status in ["open", "closed", "in progress", "need info"]

# вызов валидатора validators=[status_validator]

class sell_items(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название"),
    description = models.TextField(verbose_name="Описание"),
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена"),
    shop_id = models.ForeignKey(shop, on_delete=models.RESTRICT, verbose_name="Магазин") 
    
class shop(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название"),
    description = models.TextField(verbose_name="Описание"),
    user_id = models.ForeignKey(user_data, on_delete=models.RESTRICT, verbose_name="Владелец магазина") 

class user_data(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя пользователя"),
    name = models.CharField(max_length=50, verbose_name="Имя пользователя"),
    description = models.TextField(verbose_name="Описание"),
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена"),
    shop_id = models.ForeignKey(shops, on_delete=models.RESTRICT, verbose_name="Магазин") 
    
    
