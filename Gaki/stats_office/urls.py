from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "stats_main"),
    path('sell', views.sells, name = "stats_sells"),
]