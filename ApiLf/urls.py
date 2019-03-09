
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from api import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('api/(?P<version>\w+)/', include('api.urls')),
]
