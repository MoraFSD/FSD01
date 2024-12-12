from .models import sell_item, shop
from django import forms

class FilterForm(forms.Form):

    filter_start = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'type': 'date',  # Используйте HTML5 тип date для ввода даты
        'class': 'form-control fs-6 rounded border-opacity-50',  # Добавьте классы для стилей, если требуется
    }))
    filter_end = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'type': 'date',  # Используйте HTML5 тип date для ввода даты
        'class': 'form-control fs-6 rounded border-opacity-50',  # Добавьте классы для стилей, если требуется
    }))
    filter_item = forms.ModelMultipleChoiceField(
        queryset=sell_item.objects.none(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-text fs-6 rounded border border-0',  # Добавьте класс для стилизации
            'size': 5,  # Установите размер виджета, чтобы отобразить несколько элементов
        }),
        label="Выберите название"
    )
    filter_shop = forms.ModelMultipleChoiceField(
        queryset=shop.objects.none(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-text fs-6 rounded border border-0',  # Добавьте класс для стилизации
            'size': 5,  # Установите размер виджета, чтобы отобразить несколько элементов
        }),
    )

class UploadShopForm(forms.ModelForm):
    class Meta:
        model = shop
        fields = ['name', 'description', 'user_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название магазина'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание магазина'})
        }

class UploadItemForm(forms.ModelForm):
    shop_id = forms.ModelChoiceField(
        queryset=shop.objects.none(), 
        to_field_name='name', 
        widget=forms.Select(attrs={ 'class': 'form-control', 'placeholder': 'Магазин'})
    )
    
    class Meta:
        model = sell_item
        fields = ['name', 'description', 'price', 'shop_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание товара'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Стоимость товара'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(self.fields['shop_id'].queryset)  # Для отладки