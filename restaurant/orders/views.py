from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.template import RequestContext

from .models import MenuItem
from orders.forms import CustomerForm, AddressForm


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
            return redirect("home")
        #user = User(username=request.POST.username)
    return render_to_response("registration/create_user.html", context,
                              context_instance=RequestContext(request))
