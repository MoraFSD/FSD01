from django.shortcuts import render
from django.http import HttpResponse
from . import models, forms
from .forms import FilterForm
from django.db.models import Sum
import csv
import io

def index(request):
    form = FilterForm()
    sells_table = models.sell.objects.all()
    sells_item = models.sell_item.objects.all()
    current_user = request.user
    user_name = current_user.username 
    
    sells_table = sells_table.filter(item_id__shop_id__user_id__name=user_name)
    form.fields['filter_shop'].queryset = models.shop.objects.filter(user_id__name=user_name)
    form.fields['filter_item'].queryset = models.sell_item.objects.filter(shop_id__user_id__name=user_name)
    
    if request.method == 'POST':
        form = FilterForm(request.POST)
        

        if user_name:
            form.fields['filter_shop'].queryset = models.shop.objects.filter(user_id__name=user_name)
            form.fields['filter_item'].queryset = models.sell_item.objects.filter(shop_id__user_id__name=user_name)

        if form.is_valid():
            start_date = form.cleaned_data.get('filter_start')
            end_date = form.cleaned_data.get('filter_end')
            titles = form.cleaned_data.get('filter_item')
            shops = form.cleaned_data.get('filter_shop')
            
        # Фильтрация по дате
        if start_date:
            sells_table = sells_table.filter(sell_date__gte=start_date)
        if end_date:
            sells_table = sells_table.filter(sell_date__lte=end_date)

        # Фильтрация по названиям
        if titles:
            sells_table = sells_table.filter(item_id__in=titles)

        # Фильтрация по магазинам
        # if shops:
        #     sells_table = sells_table.filter(item_id__shop_id__in=shops)

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
    form_shop = forms.UploadShopForm()
    form_item = forms.UploadItemForm()
    current_user = request.user
    user_name = current_user.username 

    form_item.fields['shop_id'].queryset = models.shop.objects.filter(user_id__name=user_name)

    if request.method == "POST":
        if 'item_form' in request.POST:
            form_item = forms.UploadItemForm(request.POST)
            form_item.fields['shop_id'].queryset = models.shop.objects.filter(user_id__name=user_name)

            if form_item.is_valid():
                form_item.save()
                return HttpResponse("Загружено")
            else:  print(form_item.errors, form_item.fields['shop_id'].queryset)




        if 'csv_form' in request.POST:
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                return HttpResponse("Файл не является CSV.")
            
            # Чтение CSV файла
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string, delimiter=',')
            next(reader)  # Пропустить заголовок, если он есть

            for row in reader:
                user = models.user_data.objects.get(name=row[1])
                print(user)
                item = models.sell_item.objects.get(name=row[2])
                print(item)

                _, created = models.sell.objects.update_or_create(
                    sell_date=row[0],
                    user_id=models.user_data.objects.get(name=row[1]), 
                    item_id=models.sell_item.objects.get(name=row[2])
                )
            return HttpResponse('Загружено')
            print(f"Создан новый объект UserData: {user_data}")

        if 'shop_form' in request.POST:
            form_shop = forms.UploadShopForm(request.POST)
            if models.user_data.objects.filter(name=user_name).exists():
                post_data = request.POST.copy()
                post_data['user_id'] = models.user_data.objects.get(name=user_name)
                form_shop = forms.UploadShopForm(post_data)
                # form_shop.fields['user_id'].initial = models.user_data.objects.get(name=user_name)  # Устанавливаем начальное значение
                print(f"Установлено начальное значение: {form_shop.fields['user_id']}")
            else:
                user_datacheck = models.user_data.objects.create(name=user_name)
                print(f"Создан новый объект UserData: {user_datacheck}")
                post_data = request.POST.copy()
                post_data['user_id'] = models.user_data.objects.get(name=user_name)
                form_shop = forms.UploadShopForm(post_data)
            
            if form_shop.is_valid():
                form_shop.save()
                return HttpResponse("Загружено")
            else:
                print(form_shop.errors, form_shop.fields['user_id'].initial)
                print(request.POST)
            
        



    data={
        'form_shop' : form_shop,
        'form_item' : form_item,
        'user_name' : user_name,
    }
    return render(request, 'Gaki\import.html', data)

def user_login(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        
        if form.is_valid():
            start_date = form.cleaned_data.get('filter_start')
            end_date = form.cleaned_data.get('filter_end')
            titles = form.cleaned_data.get('filter_item')
    return render(request, '')

def user_registration(request):
    
    return render(request, '')
