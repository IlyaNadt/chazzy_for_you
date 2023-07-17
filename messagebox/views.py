from django.shortcuts import render, get_object_or_404
from .models import Message

def messagebox_view(request):
    messages = Message.objects.all()
    return render(request, 'messagebox.html', {'messages': messages})

def message_view(request,year, month, day, message):
    message = Message.get_object_or_404(Message, slug=message)
    return render(request, 'message.html', {'message': message})
