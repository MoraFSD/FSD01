from django.shortcuts import render
from django.http import HttpResponse
from . import models 
from .forms import FilterForm
from django.db.models import Sum

def index(request):
    form = FilterForm()
    sells_table = models.sell.objects.all()
    sells_item = models.sell_item.objects.all()
     
    
    if request.method == 'POST':
        form = FilterForm(request.POST)
        
        if form.is_valid():
            start_date = form.cleaned_data.get('filter_start')
            end_date = form.cleaned_data.get('filter_end')
            titles = form.cleaned_data.get('filter_item')
            
        # Фильтрация по дате
        if start_date:
            sells_table = sells_table.filter(sell_date__gte=start_date)
        if end_date:
            sells_table = sells_table.filter(sell_date__lte=end_date)

        # Фильтрация по названиям
        if titles:
            sells_table = sells_table.filter(item_id__in=titles)

    total_count = sells_table.count()
    total_price = sells_table.aggregate(total=Sum('item_id__price'))
    
    #data
    data = {
        'sells_table' : sells_table,
        'sells_item' : sells_item,
        'form' : form,
        'total_price' : total_price['total'],
        'total_count' : total_count
    }
    return render(request, 'Gaki\index.html', data)
    

def sells(request):
    
    print (sells_table)
    return render(request, 'Gaki\index.html')

def data_import(request):

    return render(request, 'Gaki\index.html')
