from django.conf.urls import url

from accounts.serializers import CustomJWTSerializer
from accounts.rest_views import JSONWebTokenAPIOverride

urlpatterns = [
    url(r'^login/$', JSONWebTokenAPIOverride.as_view(serializer_class=CustomJWTSerializer)),
    
]
