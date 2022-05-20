from rest_framework import generics
from rest_framework.response import Response
from .serializer import MessageSerializer
from .models import Message

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse



from django.utils import timezone

class MessageCreateApi(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageApi(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDeleteApi(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

@api_view(['POST'])
def createMessage(request):
    a = timezone.now() - timezone.timedelta(hours=1)
    filtered = Message.objects.filter(created_at__gte=a)
    if filtered.count() < 10:
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
            return JsonResponse({ 'message' : 'Not Allowed'})
            
   