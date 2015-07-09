from django.shortcuts import render, render_to_response

# Create your views here.
def HomeView(request):
    return render_to_response("base.html", )