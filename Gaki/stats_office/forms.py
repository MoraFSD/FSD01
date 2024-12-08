from .models import sell_item
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
        queryset=sell_item.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-text fs-6 rounded border border-0',  # Добавьте класс для стилизации
            'size': 5,  # Установите размер виджета, чтобы отобразить несколько элементов
        }),
        label="Выберите название"
    )