from django.urls import path
from . import views

urlpatterns = [
    path("messagebox_home", views.messagebox_home, name='messagebox_home'),
    path("<int:pk>", views.message_detail, name='message'),
]

app_name = 'messagebox'
