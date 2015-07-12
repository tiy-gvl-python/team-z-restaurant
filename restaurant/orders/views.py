from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.template import RequestContext
from .models import MenuItem, Order, CartOption
from orders.decorators import require_owner
from orders.forms import CustomerForm, AddressForm, OwnerForm, RestaurantForm


class RequireOwnerMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RequireOwnerMixin, cls).as_view(**initkwargs)
        return require_owner(view)


class CreateMenuItemView(RequireOwnerMixin, CreateView):
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


class CreateOrderView(CreateView):
    model = Order
    success_url = reverse_lazy("create_order")
    template_name = 'create_order_item.html'
    fields = ["restaurant", "customer", "instructions"]


class DeleteOrderView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')


class UpdateOrderView(UpdateView):
    model = Order
    template_name = "update_order_list.html"
    fields = ["restaurant", "customer", "instructions"]
    success_url = reverse_lazy('order_list')


class CartOptionUpdateView(UpdateView):
    model = CartOption
    template_name = "update_cart_option_view.html"
    fields = ["menu_item", "order", "count"]
    success_url = reverse_lazy('order_list')

    def get_success_url(self):
        return self.success_url + str(self.object.order.id)


class CartOptionCreateView(CreateView):
    model = CartOption
    template_name = "create_cart_option_view.html"
    fields = ["menu_item", "order", "count"]
    success_url = reverse_lazy('order_list')

    def get_success_url(self):
        return self.success_url + str(self.object.order.id)


class CartOptionDeleteView(DeleteView):
    model = CartOption
    success_url = reverse_lazy('order_list')

    def get_success_url(self):
        return self.success_url + str(self.object.order.id)


@require_owner
def owner_registration_view(request):
    context = {"user_form": UserCreationForm, "owner_form": OwnerForm, "errors": []}
    if request.POST:
        valid = True
        user_form = UserCreationForm(request.POST)
        owner_form = OwnerForm(request.POST)
        if not user_form.is_valid():
            valid = False
            context["errors"].append("Invalid Username or Password.")
        if not owner_form.is_valid():
            valid = False
            context["errors"].append("Invalid Name, Telephone or Email.")
        if valid:
            user = user_form.save()
            owner = owner_form.save(commit=False)
            owner.user = user
            owner.save()
    return render_to_response('owner_registration.html', context=context,
                              context_instance=RequestContext(request))


def restaurant_creation_view(request):
    context = {"restaurant_form": RestaurantForm, "address_form": AddressForm, "errors": []}
    if request.POST:
        valid = True
        restaurant_form = RestaurantForm(request.POST)
        address_form = AddressForm(request.POST)
        if not restaurant_form.is_valid():
            valid = False
            context["errors"].append("Invalid Name or Telephone.")
        if not address_form.is_valid():
            valid = False
            context["errors"].append("Invalid address.")
        if valid:
            address = address_form.save()
            restaurant = restaurant_form.save(commit=False)
            restaurant.address = address
            restaurant.save()
    return render_to_response('restaurant_creation.html', context=context,
                              context_instance=RequestContext(request))
