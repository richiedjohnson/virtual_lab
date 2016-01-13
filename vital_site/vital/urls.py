from django.conf.urls import url

from . import views

app_name = 'vital'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^courses/(?P<course_id>[0-9]+)/faculties/$', views.course_faculty, name='course_faculty'),
    url(r'^courses/(?P<course_id>[0-9]+)/register/$', views.register_for_course, name='register_for_course'),
    url(r'^users/register/$', views.register, name='register'),
]