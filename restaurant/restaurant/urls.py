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
from django.contrib.auth.views import login, logout
import django_cryptocoin.urls as cryptocoin

from orders import views

urlpatterns = [
    url(r'^register/$', views.registration_view,
        name="register"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/$', views.MenuListView.as_view(), name="menu_list"),
    url(r'^menu/(?P<pk>\d+)/$', views.MenuDetailView.as_view(), name='menu_detail'),
    url(r'^$', views.home_view, name="home"),
    url(r'^login/', login, name="login",
        kwargs={"template_name": "login.html", "redirect_field_name": "redirect"}),
    url(r'^logout/$', logout, name='logout',
        kwargs={'next_page': '/'}),
    url(r'^create_menu_item/', views.CreateMenuItemView.as_view(), name='create_menu_item'),
    url(r'^delete_menu_item/(?P<pk>\d+)/', views.DeleteMenuItemView.as_view(), name='delete_menu_item'),
    url(r'^update_menu_item/(?P<pk>\d+)/', views.UpdateMenuItemView.as_view(), name='update_menu_item'),
    url(r'^orders/$', views.OrderListView.as_view(), name="order_list"),
    url(r'^orders/(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name='order_detail'),
    url(r'^create_order_view/$', views.CreateOrderView.as_view(), name='create_order'),
    url(r'^delete_order_view/(?P<pk>\d+)/', views.DeleteOrderView.as_view(), name='delete_order'),
    url(r'^update_order_view/(?P<pk>\d+)/', views.UpdateOrderView.as_view(), name='update_order'),
    url(r'^cart_option_update_view/(?P<pk>\d+)/', views.CartOptionUpdateView.as_view(), name='update_cart_options'),
    url(r'^cart_option_create_view/', views.CartOptionCreateView.as_view(), name='create_cart_options'),
    url(r'^cart_option_delete_view/(?P<pk>\d+)/', views.CartOptionDeleteView.as_view(), name='delete_cart_options'),
    url(r'^register/owner$', views.owner_registration_view, name='owner_registration'),
    url(r'^create_restaurant/', views.restaurant_creation_view, name='create_restaurant'),
    url(r'^profile/', views.CustomerProfileView.as_view(), name='customer_profile'),
    url(r'^user_list/$', views.CustomerListView.as_view(), name='customer_list'),
    url(r'^user_list/(?P<pk>\d+)/$', views.CustomerDetailView.as_view(), name='customer_detail'),
    url(r'^owners/$', views.OwnerListView.as_view(), name="owner_list"),
    url(r'^owners/(?P<pk>\d+)/', views.OwnerDetailView.as_view(), name="owner_detail"),
    url(r'^owners/update/(?P<pk>\d+)/', views.UpdateOwnerView.as_view(), name="update_owner"),
    url(r'^restaurants/$', views.RestaurantListView.as_view(), name="restaurant_list"),
    url(r'^restaurants/(?P<pk>\d+)/', views.RestaurantDetailView.as_view(), name="restaurant_detail"),
    url(r'^restaurants/update/(?P<pk>\d+)/', views.UpdateRestaurantView.as_view(), name="update_restaurant"),
    url(r'^orders/(?P<pk>\d+)/payment', views.payment_view, name="payment"),
    url(r'^payment_processing', include(cryptocoin),name="cryptocoin")
]
