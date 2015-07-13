from decimal import Decimal, ROUND_HALF_UP
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.template import RequestContext
from django_cryptocoin.models import CryptoOrder, ExchangeRate
from django_cryptocoin.settings import CRYPTO_COINS
from .models import MenuItem, Order, CartOption, Customer, Owner, Restaurant
from orders.decorators import require_owner, provide_customer, require_customer
from orders.forms import CustomerForm, AddressForm, OwnerForm, RestaurantForm, OrderPaymentForm
import django_cryptocoin.views as cryptocoin


class ProvideCurrentCustomer:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(ProvideCurrentCustomer, cls).as_view(**initkwargs)
        return provide_customer(view)


class RequireOwnerMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RequireOwnerMixin, cls).as_view(**initkwargs)
        return require_owner(view)

class RequireCustomerMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RequireCustomerMixin, cls).as_view(**initkwargs)
        return require_customer(view)

class AddCustomerToFormMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.customer = self.request.user.customer
        return super(AddCustomerToFormMixin, self).form_valid(form)


class AddOrderToFormMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.order = self.request.user.customer.order_set.all().order_by("-id")[0]
        return super(AddOrderToFormMixin, self).form_valid(form)


class CreateMenuItemView(RequireOwnerMixin, CreateView):
    model = MenuItem
    template_name = 'create_menu_item.html'
    success_url = reverse_lazy("menu_list")
    fields = ["title", "description", "price", "menu_parts"]


class DeleteMenuItemView(RequireOwnerMixin, DeleteView):
    model = MenuItem
    success_url = reverse_lazy('menu_list')


class UpdateMenuItemView(RequireOwnerMixin, UpdateView):
    model = MenuItem
    template_name = "update_menu_item.html"
    fields = ["title", "description", "price", "menu_parts"]
    success_url = reverse_lazy('menu_list')


def MenuListView(request):
    app = MenuItem.objects.filter(menu_parts='Appetizer')
    entree = MenuItem.objects.filter(menu_parts='Entree')
    des = MenuItem.objects.filter(menu_parts='Dessert')
    drink = MenuItem.objects.filter(menu_parts='Drink')
    context = {'appetizer': app, 'entree': entree, 'dessert': des, 'drink': drink}
    return render_to_response('menu_list_view2.html', context, context_instance=RequestContext(request))


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


class CreateOrderView(RequireCustomerMixin, AddCustomerToFormMixin, CreateView):
    model = Order
    success_url = reverse_lazy("order_list")
    template_name = 'create_order_item.html'
    fields = ["restaurant"]

    def get_success_url(self):
        return self.success_url + str(self.object.id)


class DeleteOrderView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')


class UpdateOrderView(UpdateView):
    model = Order
    template_name = "update_order_list.html"
    fields = ["restaurant"]
    success_url = reverse_lazy('order_list')


class CartOptionUpdateView(AddOrderToFormMixin, UpdateView):
    model = CartOption
    template_name = "update_cart_option_view.html"
    fields = ["menu_item", "quantity"]
    success_url = reverse_lazy('order_list')

    def get_success_url(self):
        return self.success_url + str(self.object.order.id)


class CartOptionCreateView(AddOrderToFormMixin, CreateView):
    model = CartOption
    template_name = "create_cart_option_view.html"
    fields = ["menu_item", "quantity"]
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
            return redirect("owner_list")
    return render_to_response('owner_registration.html', context=context,
                              context_instance=RequestContext(request))


@require_owner
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
            redirect('restaurant_list')
    return render_to_response('restaurant_creation.html', context=context,
                              context_instance=RequestContext(request))


class CustomerProfileView(ProvideCurrentCustomer, UpdateView):
    """Actually an update view"""
    model = Customer
    template_name = "customer_profile.html"
    fields = ["name", "email", "telephone"]
    success_url = reverse_lazy("customer_profile")


class CustomerListView(RequireOwnerMixin, ListView):
    model = Customer
    template_name = "customer_list_view.html"


class CustomerDetailView(RequireOwnerMixin, DetailView):
    model = Customer
    template_name = "customer_detail_view.html"


class OwnerListView(RequireOwnerMixin, ListView):
    model = Owner
    template_name = "owner_list.html"



class UpdateOwnerView(RequireOwnerMixin, UpdateView):
    model = Owner
    template_name = "update_owner.html"
    fields = ["name", "telephone"]
    success_url = reverse_lazy('owner_list')


class OwnerDetailView(RequireOwnerMixin, DetailView):
    model = Owner
    template_name = "owner_detail.html"


class RestaurantListView(ListView):
    model = Restaurant
    template_name = "restaurant_list.html"


class UpdateRestaurantView(RequireOwnerMixin, UpdateView):
    model = Restaurant
    template_name = "update_restaurant.html"
    fields = ["name", "telephone", "owner"]
    success_url = reverse_lazy('restaurant_list')


class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = "restaurant_detail.html"


@require_customer
def payment_view(request, pk):
    order = Order.objects.filter(id=pk)
    if not order or order.get().customer.user.id != request.user.id:
        return redirect("home")
    order = order.get()
    price_usd = Decimal(sum([cart_option.menu_item.price * cart_option.quantity
                             for cart_option in order.cartoption_set.all()]))
    try:
        rate = ExchangeRate.get_exchange_rate('usd', 'btc')
    except BaseException as e:
        rate = 1
    crypto_prices = {'btc': Decimal(price_usd * rate).quantize(Decimal(10) ** -5, rounding=ROUND_HALF_UP)}
    if request.POST:
        print("post")
        form = OrderPaymentForm(request.POST)
        if form.is_valid():
            crypto_order = CryptoOrder(
                currency=form.cleaned_data['currency'],
                amount=crypto_prices[form.cleaned_data['currency']],
                date=timezone.now(),
                redirect_to='home'
            )
            crypto_order.save()
            form.instance.crypto_order = crypto_order
            form.instance.customer = order.customer
            form.save()
            return redirect(cryptocoin.process, addr=crypto_order.addr)
    else:
        form = OrderPaymentForm(initial={"id": order.id, "restaurant": order.restaurant})
    context = {'form': form, 'crypto_prices': crypto_prices, 'order': order}
    return render_to_response('payment.html', context=context,
                              context_instance=RequestContext(request))

@require_owner
def management_options_view(request):
    return render_to_response('management_options.html', context_instance=RequestContext(request))

