from django.conf.urls import url

from imageupload import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^logout$', views.handle_logout, name='logout'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^upload/(?P<ui_id>[0-9]+)$', views.upload_result, name='upload_result'),
]