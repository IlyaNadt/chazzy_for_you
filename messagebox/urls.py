from django.urls import path
from . import views

urlpatterns = [
    path("messagebox/", views.messagebox_view, name='messagebox_view'),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", views.message_view, name='message_view'),
]

