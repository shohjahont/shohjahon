from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
class AbuotPageView(TemplateView):
    template_name = 'about.html'
class ChiqishPageview(TemplateView):
    template_name = 'chiqish.html'
