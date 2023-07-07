from django.urls import path
from .views import HomePageView, AboutPageView, MessageboxPageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("contacts/", AboutPageView.as_view(), name='contacts'),
    path("messagebox/", MessageboxPageView.as_view(), name='messagebox')
]