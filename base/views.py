from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from messagebox.models import Message

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "contacts.html"

class MessageboxPageView(ListView):
    model = Message
    template_name = "messagebox.html"