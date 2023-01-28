from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from uncraftedapi.models import Message, User
from rest_framework.decorators import action
from rest_framework import generics

class MessageSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'subject',
                  'message_content', 'is_new', 'connected_to_trade')
        depth = 1


class MessageView(ViewSet):

    def retrieve(self, request, pk):
        message = Message.objects.get(pk=pk)
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    def list(self, request):
        messages = Message.objects.all()
        user = request.query_params.get('sender', None)
        if user is not None:
            messages = messages.filter(uid = user.uid)
        user = request.query_params.get('receiver', None)
        if user is not None:
            messages = messages.filter(uid = user.uid)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def create(self, request):
        sender = User.objects.get(uid = request.data["sender"])
        receiver = User.objects.get(uid = request.data["receiver"])
        message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            subject=request.data["subject"],
            message_content=request.data["message_content"],
            is_new=request.data["is_new"],
            connected_to_trade=request.data["connected_to_trade"],
        )
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    def update(self, request, pk):
        message = Message.objects.get(pk=pk)
        sender = User.objects.get(uid = request.data["sender"])
        receiver = User.objects.get(uid = request.data["receiver"])
        message.sender = sender
        message.receiver = receiver
        message.subject = request.data["subject"]
        message.message_content = request.data["message_content"]
        message.is_new = request.data['is_new']
        message.connected_to_trade = request.data['connected_to_trade']
        message.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        message = Message.objects.get(pk=pk)
        message.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserMessageView(generics.ListCreateAPIView):
  serializer_class = MessageSerializer

  def get_queryset(self):
    sender_id = self.kwargs['sender_id']
    return Message.objects.filter(sender__id=sender_id)
