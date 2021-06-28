from django.urls import path
from .views import HomePageView, AbuotPageView, ChiqishPageview
urlpatterns = [
    path('Chiqish/', ChiqishPageview.as_view(), name = 'Chiqish'),
    path('about/', AbuotPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name='home'),
]