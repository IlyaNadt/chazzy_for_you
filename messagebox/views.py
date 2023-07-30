from django.shortcuts import render, get_object_or_404
from .models import Message
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def messagebox_home(request):
    object_list = Message.objects.all()
    paginator = Paginator(object_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'messagebox/messagebox_home.html', {'page_obj': page_obj})

def message_detail(request, pk):
    return render(request, 'messagebox/message.html', {'message': get_object_or_404(Message, pk=pk)})