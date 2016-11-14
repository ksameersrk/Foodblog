from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post', views.post_list, name='post_list'),
    url(r'^signup', views.post_new, name='post_new'),
    url(r'^login', views.post_old, name='post_old'),
    url(r'^write', views.post_write, name='post_write'),
]