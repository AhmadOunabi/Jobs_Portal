from django.shortcuts import render
from django.views import generic
from .models import Jobs,Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import UserSerializer
from django.contrib.auth.models import User
# Create your views here.

class ProductList(generic.ListView):
    model = Jobs



class RegisterAPIVIEW(APIView):
    def post(self,request):
        data= request.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('passwords dont match!')
        serializer=UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginAPIVIEW(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        user=User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('email or password is incorrect')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('email or password is incorrect')
        serializer= UserSerializer(user)
        return Response(serializer.data)
        
        