from django.urls import path
from .views import HomePageView, AbuotPageView
urlpatterns = [
    path('about/', AbuotPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name='home'),
]