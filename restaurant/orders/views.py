from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.template import RequestContext

from .models import MenuItem


class CreateMenuItem(CreateView):
    model = MenuItem
    success_url = ''
    fields = ["title", "description", "price"]


class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu_list_view.html'


class MenuDetailView(DetailView):
    model = MenuItem
    template_name = 'menu_detail_view.html'


def home_view(request):
    return render_to_response("base.html", context_instance=RequestContext(request))
