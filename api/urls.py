from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from api.views import course

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('course/$', course.CourseView.as_view()),
]
