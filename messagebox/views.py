from django.shortcuts import render, get_object_or_404
from .models import Message

def messagebox_home(request):
    messagebox = Message.objects.all()
    return render(request, 'messagebox/messagebox_home.html', {'messagebox': messagebox})

def message_detail(request, pk):
    message = Message.get_object_or_404(pk=pk)
    return render(request, 'messagebox/message.html', {'message': message})