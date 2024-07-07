from django.urls import path
from . import views

urlpatterns = [
  path('', views.test_page, name='test_page'),
  path('test_page2', views.test_page2, name='test_page2'),
]