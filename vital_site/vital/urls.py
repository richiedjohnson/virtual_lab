from django.conf.urls import url

from . import views

app_name = 'vital'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/id/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^courses/register/$', views.register_for_course, name='course_register'),
    url(r'^courses/registered/$', views.registered_courses, name='registered_courses'),
    url(r'^users/register/$', views.register, name='user_register'),
    url(r'^users/activate/$', views.activate, name='user_activate'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^users/reset-password', views.reset_password, name='user_reset_password'),
    url(r'^users/forgot-password', views.forgot_password, name='user_forgot_password'),
]