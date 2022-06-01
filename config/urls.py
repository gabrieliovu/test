from django.urls import re_path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Documentation')

urlpatterns = [
    re_path(r'^$', schema_view),
    re_path(r'^api/', include('users.urls'))
]
