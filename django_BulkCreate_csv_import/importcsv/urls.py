from django.contrib.auth import views
from django.urls import path
from .views import EmployeeUploadView
from .views import get_productos

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('importar_productos/', EmployeeUploadView.as_view(), name='importar_productos'),
    path('ver_productos/', get_productos, name='ver_productos')
]