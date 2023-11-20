from django.urls import path
from .import views 

urlpatterns = [
    path('chatmethod',views.chatmethod.as_view(),name="chatmethod")
]
