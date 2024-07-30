import category as category
import django_filters
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter, CharFilter
from .models import Post, Response
from django.forms import DateTimeInput, DateInput


class PostFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок'
    )

    categoryType = django_filters.ModelChoiceFilter(
        field_name='category',
        queryset=category.objects.all(),
        label='Категории',
        empty_label='Выберите категорию ',
    )

    dateCreation_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
