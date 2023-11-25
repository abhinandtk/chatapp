from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .pusher import pusher_client
from django.contrib.auth.models import User
from .models import chat
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from .serializers import chatserializer


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
    
class Login(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return Response({'data':user.id,'message':'Login successfully'})
        else:
            return Response('Login Failed')

class chatapi(APIView):
    def post(self,request):
      from_user=request.data.get('from_user')
      to_user=request.data.get('to_user')
      message=request.data.get('message')
      messagedata=chat.objects.create(from_user_id=from_user,to_user_id=to_user,message=message)
      return Response('success')

class getuserall(APIView):
    def get(self,request):
        data=User.objects.all().exclude(is_superuser=True).order_by('id')
        print(data)
        for i in data:
            print(i.id)
        return Response('success')

class inbox(APIView):
    def post(self, request):
        from_user = request.data.get('from_user')
        print('------', request.data)

        user_send = chat.objects.filter(Q(from_user=from_user) | Q(to_user=from_user))

        unique_send_usernames = set()
        unique_receive_usernames = set()  # Use a set to keep track of unique user IDs

        for message in user_send:
            if message.from_user_id == int(from_user):
                unique_send_usernames.add(message.to_user.id)
            else:
                unique_receive_usernames.add(message.from_user.id)

        # Convert set of unique user IDs to a list of dictionaries
        unique_send_usernames = [{'id': user_id, 'username': User.objects.get(id=user_id).username} for user_id in unique_send_usernames]
        unique_receive_usernames = [{'id': user_id, 'username': User.objects.get(id=user_id).username} for user_id in unique_receive_usernames]

        response_data = {
            'send_usernames': unique_send_usernames,
            'receive_usernames': unique_receive_usernames,
        }

        return Response({'data': response_data})

class user_chat(APIView):
    def post(self,request):
        from_user=request.data.get('from_user')    
        to_user=request.data.get('to_user')
        send=chat.objects.filter(from_user=from_user,to_user=to_user)
        receive=chat.objects.filter(to_user=from_user,from_user=to_user)
        sendmessages=[{'message':i.message,'name':i.from_user_id,'date':i.create_date} for i in send]
        receivemessages = [{'message': i.message, 'name': i.from_user_id,'date':i.create_date} for i in receive]

        return Response({'send':sendmessages,'receive':receivemessages})





