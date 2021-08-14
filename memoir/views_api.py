from typing import Match
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from .helpers import *
from django.contrib.auth import authenticate , login 
from memoir.helpers import generate_random_string

import re



class LoginView(APIView):


    def post(self , request): 
        response = {}
        response['status'] = 500
        response['message'] ='Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            
            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['message'] = 'invalid username not found'
                raise Exception('invalid username  not found')

            """if not Profile.objects.filter(user = check_user).first().is_verified:
                response['message'] = 'your profile is not verified'
                raise Exception(' profile is not verified')"""

            user_obj = authenticate(username = data.get('username') , password = data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password')



        except Exception as e :
            print(e)

        return Response(response)

LoginView = LoginView.as_view()


class RegisterView(APIView):
    

    def post(self , request): 
        response = {}
        response['status'] = 500
        response['message'] ='Something went wrong'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('email') is None:
                response['message'] = 'key Email not found'
                raise Exception('key Email not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            
            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user:
                response['message'] = 'username is already taken'
                raise Exception('username is already taken')

            
            
            """regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                check_mail = (re.fullmatch(regex, 'email'))
     
                # pass the regular expression
                # and the string into the fullmatch() method
                if check_mail is None:
                response['message'] = 'invalid email'
                raise Exception('invalid email')
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                 if (re.fullmatch(regex, 'email'))= None:
                  response['message'] = 'invalid email'
                 aise Exception('invalid email')"""
                 
           
                

            user_obj = User.objects.create(username = data.get('username') , email = data.get('email'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            """token = generate_random_string(20)
            Profile.objects.create(user = user_obj , token = token)
            send_mail_to_user(token , data.get('email'))"""
            response['message'] = 'User Created'
            response['status'] = 200



        except Exception as e :
            print(e)

        return Response(response)

RegisterView = RegisterView.as_view()