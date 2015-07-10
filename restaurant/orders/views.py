from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.template import RequestContext

from .models import MenuItem


class CreateMenuItemView(CreateView):
    model = MenuItem
    template_name = 'create_menu_item.html'
    success_url = reverse_lazy("menu_list")
    fields = ["title", "description", "price", "menu_parts"]


class DeleteMenuItemView(DeleteView):
    model = MenuItem
    success_url = reverse_lazy('menu_list')

class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu_list_view.html'


class MenuDetailView(DetailView):
    model = MenuItem
    template_name = 'menu_detail_view.html'


def home_view(request):
    return render_to_response("base.html", context_instance=RequestContext(request))
