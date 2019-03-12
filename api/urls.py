from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from api.views import course
from api.views import account

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^course/$', course.CourseView.as_view({'get': 'list'})),

    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get': 'retrieve'})),



    url(r'^authfl/$', account.AuthView.as_view()),
    url(r'^micro/$', course.MicroView.as_view()),
]
