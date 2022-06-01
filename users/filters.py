from urllib.parse import unquote

from django.db.models import Q
from django_filters.rest_framework import FilterSet, CharFilter, DateFilter, NumberFilter

from users.models import Person


class PersonFilterSet(FilterSet):
    query = CharFilter(method='filter_by_query')
    gender = CharFilter(field_name='gender', lookup_expr='exact')
    industry = CharFilter(field_name='industry', lookup_expr='exact')
    date_of_birth__gte = DateFilter(field_name='date_of_birth', lookup_expr='gte')
    date_of_birth__lte = DateFilter(field_name='date_of_birth', lookup_expr='lte')
    years_of_experience__gte = NumberFilter(field_name='years_of_experience', lookup_expr='gte')
    years_of_experience__lte = NumberFilter(field_name='years_of_experience', lookup_expr='lte')
    salary__gte = NumberFilter(field_name='salary', lookup_expr='gte')
    salary__lte = NumberFilter(field_name='salary', lookup_expr='lte')

    class Meta:
        model = Person
        fields = []

    @staticmethod
    def filter_by_query(queryset, _, value):
        value = unquote(value)
        search_terms = value.split()
        qs_filter = Q()

        for search_term in search_terms:
            search_term = search_term.strip()
            if not search_term:
                continue

            qs_filter &= (
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(email__icontains=search_term) |
                Q(industry__icontains=search_term)
            )

        return queryset.filter(qs_filter).distinct()
