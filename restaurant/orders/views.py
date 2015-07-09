from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import FoodItem


class CreateMenuItem(CreateView):
    model = FoodItem
    success_url = ''
    fields = ["title", "description", "price"]


class MenuListView(ListView):
    model = FoodItem
    template_name = 'menu_list_view.html'


class MenuDetailView(DetailView):
    model = FoodItem
    template_name = 'menu_detail_view.html'


def HomeView(request):
    return render_to_response("base.html", )
