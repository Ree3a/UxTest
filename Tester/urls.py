from django.urls import path
from Tester import views


urlpatterns = [
    path('', views.home, name='home'),
    path("tregister", views.tregister, name='tregister'),
    path('tlogin',views.tlogin, name="tlogin"),
]
