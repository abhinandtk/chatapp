from django.urls import path
from .import views 

urlpatterns = [
    path('chatmethod',views.chatmethod.as_view(),name="chatmethod"),
    path('Register',views.Register.as_view(),name="Register"),
    path('chatapi',views.chatapi.as_view(),name="chatapi"),
    path('getuserall',views.getuserall.as_view(),name="getuserall"),
    path('inbox',views.inbox.as_view(),name="inbox"),
    path('user_chat',views.user_chat.as_view(),name="user_chat"),
]
