import json

from django_filters.rest_framework import DjangoFilterBackend
from django_pandas.io import read_frame
from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Person
from users.serializers import PersonSerializer
from users.filters import PersonFilterSet


class SizablePageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 500


class PersonPagination(SizablePageNumberPagination):
    page_size = 50

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        return response


class PersonViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Person.objects.all().order_by('id')
    filter_class = PersonFilterSet
    pagination_class = PersonPagination
    serializer_class = PersonSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = '__all__'


class MeanIndustryYearsOfExperienceView(APIView):
    """
        eg: 
        {
        "industry": "Advertising",
        "years_of_experience": 26.3333333333
        },
    """
    
    def get(self, _):
        data = Person.objects.all()
        df = read_frame(data)
        data = df.groupby('industry', as_index=False)['years_of_experience'].mean()
        return Response(json.loads(data.to_json(orient="records")))


class MeanIndustrySalaryView(APIView):
    """
        eg:
        {
            "industry": "Advertising",
            "salary": 124518.4816666667
        },
    """
    def get(self, _):
        data = Person.objects.all()
        df = read_frame(data)
        data = df.groupby('industry', as_index=False)['salary'].mean()
        return Response(json.loads(data.to_json(orient="records")))


class MeanExperienceSalaryView(APIView):
    """
        eg:
         {
        "years_of_experience": 2.0,
        "salary": 133644.014
        },
    """
    def get(self, _):
        data = Person.objects.all()
        df = read_frame(data)
        data = df.groupby('years_of_experience', as_index=False)['salary'].mean()
        return Response(json.loads(data.to_json(orient="records")))


class MeanGenderSalaryView(APIView):
    """
        eg:
         {
        "gender": "F",
        "salary": 139397.4536615385
        },
    """
    def get(self, _):
        data = Person.objects.all()
        df = read_frame(data)
        data = df.groupby('gender', as_index=False)['salary'].mean()
        return Response(json.loads(data.to_json(orient="records")))


class MeanGenderIndustryYearsOfExperienceView(APIView):
    """
        eg:
        {
        "gender": "F",
        "industry": "Advertising",
        "years_of_experience": 29.5
        },
    """
    def get(self, _):
        data = Person.objects.all()
        df = read_frame(data)
        data = df.groupby(['gender', 'industry'], as_index=False)['years_of_experience'].mean()
        return Response(json.loads(data.to_json(orient="records")))


class SizeGenderIndustryYearsOfExperienceView(APIView):
    """
        eg:
        {
        "industry": "Advertising",
        "gender": "F",
        "size": 2
        },
    """
    def get(self, _):
        data = Person.objects.all()
        df = read_frame(data)
        data = df.groupby(['industry', 'gender'], as_index=False)['years_of_experience'].size()
        return Response(json.loads(data.to_json(orient="records")))
