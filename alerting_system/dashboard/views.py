from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView

# Create your views here.

class DashboardView(TemplateView):
    template_name = "dashboard/index.html"
