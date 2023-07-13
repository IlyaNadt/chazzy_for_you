from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from messagebox.models import Message

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "contacts.html"

def messagebox_view(request):
    messages = Message.objects.all()
    return render(request, 'messagebox.html', {'messages': messages})

def message_view(request,year, month, day, message):
    message = Message.get_object_or_404(Message, slug=message,\
        publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'message.html', {'message': message})
