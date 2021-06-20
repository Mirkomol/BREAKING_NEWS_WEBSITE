import django_filters
from django.forms import TextInput

from .models import *




class SearchFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices = CHOICES, method='filter_by_order')


    class Meta:
        model = Post
        fields =['title', ]


    def filter_by_order(self,queryset,name,value):
        expression = 'date_posted' if value == 'ascending' else '-date_posted'
        return queryset.order_by(expression)



class ItSearchFilter(django_filters.FilterSet):

    class Meta:
        model = It_Post
        fields =['title', ]
        widgets = {
                'title':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'

            }),
                'tags': django_filters.ChoiceFilter(attrs={
                    'class': "form-control",
                    'style': 'max-width: 300px;',
                    'placeholder': 'Name'

                })
        }


class BusinessSearchFilter(django_filters.FilterSet):

    class Meta:
        model = Business_Post
        fields =['title', ]
        widgets = {
                'title':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'

            }),
                'tags': django_filters.ChoiceFilter(attrs={
                    'class': "form-control",
                    'style': 'max-width: 300px;',
                    'placeholder': 'Name'

                })
        }



class SportSearchFilter(django_filters.FilterSet):

    class Meta:
        model = Sport_Post
        fields =['title', ]
        widgets = {
                'title':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'

            }),
                'tags': django_filters.ChoiceFilter(attrs={
                    'class': "form-control",
                    'style': 'max-width: 300px;',
                    'placeholder': 'Name'

                })
        }



class TravelSearchFilter(django_filters.FilterSet):

    class Meta:
        model = Travel_Post
        fields =['title', ]
        widgets = {
                'title':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'

            }),
                'tags': django_filters.ChoiceFilter(attrs={
                    'class': "form-control",
                    'style': 'max-width: 300px;',
                    'placeholder': 'Name'

                })
        }


