from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.template import RequestContext
from orders.forms import CustomerForm, AddressForm
from .models import MenuItem, Order


class CreateMenuItemView(CreateView):
    model = MenuItem
    template_name = 'create_menu_item.html'
    success_url = reverse_lazy("menu_list")
    fields = ["title", "description", "price", "menu_parts"]


class DeleteMenuItemView(DeleteView):
    model = MenuItem
    success_url = reverse_lazy('menu_list')


class UpdateMenuItemView(UpdateView):
    model = MenuItem
    template_name = "update_menu_item.html"
    fields = ["title", "description", "price", "menu_parts"]
    success_url = reverse_lazy('menu_list')


class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu_list_view.html'


class MenuDetailView(DetailView):
    model = MenuItem
    template_name = 'menu_detail_view.html'


def home_view(request):
    return render_to_response("base.html", context_instance=RequestContext(request))


def registration_view(request):
    context = {"user_form": UserCreationForm, "customer_form": CustomerForm, "address_form": AddressForm, "errors": []}
    if request.POST:
        valid = True
        user_form = UserCreationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        address_form = AddressForm(request.POST)
        if not user_form.is_valid():
            valid = False
            context["errors"].append("Invalid username or password.")
        if not customer_form.is_valid():
            valid = False
            context["errors"].append("Invalid name, email or telephone.")
        if not address_form.is_valid():
            valid = False
            context["errors"].append("Invalid address.")
        if valid:
            user = user_form.save()
            address = address_form.save()
            customer = customer_form.save(commit=False)
            customer.address = address
            customer.user = user
            customer.save()
            return redirect("login")
    return render_to_response("registration/create_user.html", context,
                              context_instance=RequestContext(request))


class OrderListView(ListView):
    model = Order
    template_name = 'order_list_view.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail_view.html'


