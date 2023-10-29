from django.urls import path
from .views import ProductList, RegisterAPIVIEW, LoginAPIVIEW,UserAPIVIEW,RefreshAPIVIEW,LogoutAPIVIEW,UserProfileAPIVIEW,ProfileUpdateAPIVIEW

urlpatterns = [
    path('list',ProductList.as_view()),
    path('api/register',RegisterAPIVIEW.as_view()),
    path('api/login',LoginAPIVIEW.as_view()),
    path('api/user',UserAPIVIEW.as_view()),
    path('api/refresh',RefreshAPIVIEW.as_view()),
    path('api/logout',LogoutAPIVIEW.as_view()),
    path('api/profile',UserProfileAPIVIEW.as_view()),
    path('api/profileupdate',ProfileUpdateAPIVIEW.as_view()),
]
