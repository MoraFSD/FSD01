from django.contrib import admin
from . import models

admin.site.register(models.user_data)
admin.site.register(models.shop)
admin.site.register(models.sell_item)
admin.site.register(models.sell)

