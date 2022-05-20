from django.urls import path
from .api import createMessage, MessageCreateApi, MessageApi, MessageUpdateApi, MessageDeleteApi

urlpatterns = [
    path('api',MessageApi.as_view()),
    path('api/create',createMessage),
    path('api/<int:pk>',MessageUpdateApi.as_view()),
    path('api/<int:pk>/delete',MessageDeleteApi.as_view()),
]