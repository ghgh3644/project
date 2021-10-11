from django.urls import path

from indextest import views

urlpatterns = [
    path('index/', views.test, name='test')
]