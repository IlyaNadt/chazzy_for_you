from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from messagebox.models import Message

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "contacts.html"

class MessageboxPageView(ListView):
    model = Message
    template_name = "messagebox.html"
#render branch