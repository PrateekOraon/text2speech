from django.urls import path
from django.conf.urls import url
from translate import views
from translate.views import HomePageView

urlpatterns = [
    path('', views.home, name='home'),
]