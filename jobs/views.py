import datetime
from django.shortcuts import render
from django.views import generic
from .models import Jobs,Category,UserToken,UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from .serializers import UserSerializer,UserProfileSerializer
from django.contrib.auth.models import User
from .token_generator import create_access_token,create_refresh_token,decode_access_token,decode_refresh_token
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
        
        access_token= create_access_token(user.id)
        refresh_token= create_refresh_token(user.id)
        UserToken.objects.create(
            user_id=user.id,
            token=refresh_token,
            exp_date= datetime.datetime.now() + datetime.timedelta(days=7)
        )
        
        response=Response()
        
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data={'token':access_token}
        return response


class UserAPIVIEW(APIView):
    def get(self,request):
        auth=get_authorization_header(request).split()
        if auth and len(auth)==2:
            token=auth[1].decode('utf-8')
            id= decode_access_token(token)
            user=User.objects.get(pk=id)
            if user:
                serializer=UserSerializer(user)
                return Response(serializer.data)
        raise exceptions.AuthenticationFailed('unauthenticated')


class RefreshAPIVIEW(APIView):
    def post(self,request):
        token=request.COOKIES.get('refresh_token')
        id= decode_refresh_token(token)
        user=User.objects.get(pk=id)
        if not UserToken.objects.filter(user_id=id,
                                        token=token,
                                        exp_date__gt=datetime.datetime.now()
                                        ).exists():
            raise exceptions.AuthenticationFailed('Unauthenticated')
        if user:
            access_token=create_access_token(id)
            response=Response()
            response.data={'token':access_token}
            return response

class LogoutAPIVIEW(APIView):
    def post(self,request):
        token=request.COOKIES.get('refresh_token')
        UserToken.objects.filter(token=token).delete()
        response=Response()
        response.delete_cookie(key='refresh_token')
        response.data={
            'message':'logged out successfully'
        }
        return response


class UserProfileAPIVIEW(APIView):
    def get(self,request):
        token=request.COOKIES.get('refresh_token')
        id= decode_refresh_token(token)
        user=User.objects.get(pk=id)
        profile=UserProfile.objects.get(user=user)
        data=UserProfileSerializer(profile,context={'request':request}).data
        return Response({'profile':data})
        
class ProfileUpdateAPIVIEW(APIView):
    def patch(self, request):
        token = request.COOKIES.get('refresh_token')
        id= decode_refresh_token(token)
        user=User.objects.get(pk=id)
        profile=UserProfile.objects.get(user=user)
        data=request.data
        profile.first_name= data['first_name']
        profile.last_name= data['last_name']
        profile.address= data['address']
        profile.telefon= data['telefon']
        profile.save()
        return Response('UPDATED SUCCESSFULY')
        