from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .pusher import pusher_client
from django.contrib.auth.models import User
from .models import chat

# Create your views here.
class chatmethod(APIView):
    def post(self,request):
        pusher_client.trigger('chat', 'message', {
            'username':request.data['username'],
            'message':request.data['message']
        })
        print(request.data)
        return Response([])
    
class Register(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=User.objects.create(username=username,password=password)
        user.set_password(password)
        user.save()
        return Response('registered')

class chatapi(APIView):
    def post(self,request):
      from_user=request.data.get('from_user')
      to_user=request.data.get('to_user')
      message=request.data.get('message')
      messagedata=chat.objects.create(from_user_id=from_user,to_user_id=to_user,message=message)
      return Response('success')

class getuserall(APIView):
    def get(self,request):
        data=User.objects.all().exclude(is_superuser=True)
        print(data)
        for i in data:
            print(i.id)
        return Response('success')

class inbox(APIView):
    def get(self,request):
        from_user=request.data.get('from_user')
        user=chat.objects.filter(from_user=from_user)
        print(user)
        for i in user:
            print(i.message)
        return Response('success')

class user_chat(APIView):
    def get(self,request):
        from_user=request.data.get('from_user')    
        to_user=request.data.get('to_user')
        user=chat.objects.filter(from_user=from_user,to_user=to_user)
        print(user)
        return Response('success')





