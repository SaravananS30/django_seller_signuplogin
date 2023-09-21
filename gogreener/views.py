from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.response import Response
from rest_framework.generics import *
from gogreener.serializer import *
from .models import *
from django.contrib.auth.models import User, Group, Permission
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.hashers import make_password


def index(request):
    return HttpResponse('Hello world')


class RegisterSeller(CreateAPIView):
    serializer_class = AppModelSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            serializer_class = AppModelSerializer(data=request.data)
            if serializer_class.is_valid():
                user = User.objects.create_user(request.data['seller_name'], request.data['email'],
                                                request.data['password'])
                user.save()
                hpass = make_password(request.data['password'])
                user = gogreenerapp(seller_name=request.data['seller_name'],
                                    store_name=request.data['store_name'],
                                    store_number=request.data['store_number'],
                                    email=request.data['email'],
                                    admin_share=request.data['admin_share'],
                                    password=hpass,
                                    select_city=request.data['select_city'],
                                    delivery_range=request.data['delivery_range'],
                                    store_address=request.data['store_address'],
                                    select_id=request.data['select_id'],
                                    )
                user.save()
                data = {
                    'Response Code': status.HTTP_201_CREATED,
                    'Status': 'TRUE',
                    'Message': 'User Details Created Successfully',
                    "Error": 'None',
                    "StatusFlag": True,
                    'Data': serializer_class.data,
                }
                return Response(data)
            else:
                data = {
                    'Response Code': status.HTTP_400_BAD_REQUEST,
                    'Status': 'FALSE',
                    'Message': 'Incorrect Details',
                    "Error": serializer_class.errors,
                    "StatusFlag": False,
                    'Data': [],
                }
                return Response(data)
        except Exception as e:
            data = {
                'Response Code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'Status': 'FALSE',
                'Message': 'Creating Process is failed',
                "Error": str(e),
                "StatusFlag": False,
                'Data': [],
            }
            return Response(data)


class LoginSeller(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            user = authenticate(request, email=request.data['email'], password=request.data['password'])
            if user is not None:
                token, create = Token.objects.get_or_create(user=user)
                if request.data['language'] == "":
                    Lan = 'English'
                else:
                    Lan = request.data['language']
                user = gogreenerapp.objects.filter(email=request.data['email']).update(language=Lan)
                user1 = gogreenerapp.objects.get(email=request.data['email'])
                serializer = AppModelSerializer(user1)
                data = {
                    'Response Code': status.HTTP_202_ACCEPTED,
                    'Status': 'SUCCESS',
                    'Message': 'Login Successful',
                    "Error": 'None',
                    "StatusFlag": True,
                    'Data': [serializer.data]
                }
                return Response(data)

            else:
                data = {
                    'Response Code': status.HTTP_400_BAD_REQUEST,
                    'Status': 'FALSE',
                    'Message': 'Login Failure',
                    "Error": "username or password is incorrect",
                    'Data': [],
                }
                return Response(data)
        except Exception as e:
            data = {
                'Response Code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'Status': 'FALSE',
                'Message': 'Login Process is failed',
                "Error": str(e),
                "StatusFlag": False,
                'Data': [],
            }
            return Response(data)
