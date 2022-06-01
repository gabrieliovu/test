from django.urls import re_path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from . import views


schema_view = get_swagger_view(title='Documentation')

router = routers.DefaultRouter()
router.register(r'users', views.PersonViewSet)

urlpatterns = [
    re_path(r'', include(router.urls)),
    re_path(r'mean-industry-years-of-experience/', views.MeanIndustryYearsOfExperienceView.as_view()),
    re_path(r'mean-industry-salary/', views.MeanIndustrySalaryView.as_view()),
    re_path(r'mean-experience-salary/', views.MeanExperienceSalaryView.as_view()),
    re_path(r'mean-gender-salary/', views.MeanGenderSalaryView.as_view()),
    re_path(r'mean-gender-industry-years-of-experience/', views.MeanGenderIndustryYearsOfExperienceView.as_view()),
    re_path(r'size-gender-industry-years-of-experience/', views.SizeGenderIndustryYearsOfExperienceView.as_view()),
]
