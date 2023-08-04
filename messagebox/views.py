from django.shortcuts import render, get_object_or_404
from .models import Message
from django.views.generic import ListView

class MessageListView(ListView):
    queryset = Message.objects.all()
    context_object_name = 'messagebox'
    paginate_by = 5
    template_name = 'messagebox/messagebox_home.html'

def message_detail(request, pk):
    return render(request, 'messagebox/message.html', {'message': get_object_or_404(Message, pk=pk)})
    

        


