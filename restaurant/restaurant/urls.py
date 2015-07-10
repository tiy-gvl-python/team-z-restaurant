"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout
from django.views.generic import CreateView

from orders import views

urlpatterns = [
    url(r'^registration/',
        CreateView.as_view(template_name="registration/create_user.html",
                           form_class=UserCreationForm,
                           success_url='/'),
        name="registration"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/$', views.MenuListView.as_view(), name="menu_list"),
    url(r'^menu/(?P<pk>\d+)/$', views.MenuDetailView.as_view(), name='menu_detail'),
    url(r'^$', views.home_view, name="home"),
    url(r'^login/', login, name="login",
        kwargs={"template_name": "login.html", "redirect_field_name": "redirect"}),
    url(r'^logout/$', logout, name='logout',
        kwargs={'next_page': '/'}),
    url(r'^create_menu_item/', views.CreateMenuItemView.as_view(), name='create_menu_item'),
    url(r'^delete_menu_item/(?P<pk>\d+)/', views.DeleteMenuItemView.as_view(), name='delete_menu_item')
]
