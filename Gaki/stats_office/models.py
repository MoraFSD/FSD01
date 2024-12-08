from django.db import models

def status_validator(order_status):
    return order_status in ["open", "closed", "in progress", "need info"]

# вызов валидатора validators=[status_validator]

class user_data(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя пользователя")
    email = models.EmailField(verbose_name="email")
    password = models.CharField(max_length=50, verbose_name="пароль")
    description = models.DateField(verbose_name="дата Рождения")
    first_name = models.CharField(max_length=50, verbose_name="имя", null=True)
    last_name = models.CharField(max_length=50, verbose_name="фамилия", null=True)
    patronymic = models.CharField(max_length=50, verbose_name="отчетство", null=True)
    delivery_adress = models.CharField(max_length=150, verbose_name="адрес доставки", null=True)
    inn_ur = models.CharField(max_length=10, verbose_name="ИНН юр. лица", null=True)
    inn_fiz = models.CharField(max_length=12, verbose_name="ИНН физ. лица", null=True)

    def __str__(self):
        return self.name

class shop(models.Model):
    name = models.CharField(max_length=50, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    user_id = models.ForeignKey(user_data, on_delete=models.RESTRICT, verbose_name="владелец магазина") 

    def __str__(self):
        return self.name


class sell_item(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    image = models.ImageField(verbose_name="название", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="цена")
    shop_id = models.ForeignKey(shop, on_delete=models.CASCADE, verbose_name="магазин") 

    def __str__(self):
        return self.name



class sell(models.Model):
    sell_date = models.DateField(verbose_name="дата покупки")
    user_id = models.ForeignKey(user_data, on_delete=models.SET(0), verbose_name="покупатель")
    item_id = models.ForeignKey(sell_item, on_delete=models.SET(0), verbose_name="товар")

    def __str__(self):
        
        return f"{sell_item.__str__(self.item_id)} от {self.sell_date}"


    
    
