from django.urls import path
from . import views

app_name = 'stats'
urlpatterns = [
    path('', views.index, name = 'stats_main'),
    path('sell/', views.sells, name = 'stats_sells'),
    path('import/', views.data_import, name = 'stats_data_import'),
]
