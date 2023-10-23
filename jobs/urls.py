from django.urls import path
from .views import ProductList, RegisterAPIVIEW, LoginAPIVIEW

urlpatterns = [
    path('list',ProductList.as_view()),
    path('api/register',RegisterAPIVIEW.as_view()),
    path('api/login',LoginAPIVIEW.as_view()),
]
