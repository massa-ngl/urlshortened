from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stats/<str:short_code>/', views.stats_view, name='stats_view'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
]