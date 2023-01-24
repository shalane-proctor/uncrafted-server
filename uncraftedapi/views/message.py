from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from uncraftedapi.models import Message, User
from rest_framework.decorators import action


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
        sender_id = User.objects.get(sender_id = request.data["sender_id"])
        receiver_id = User.objects.get(receiver_id = request.data["receiver_id"])
        message.sender_id = sender_id
        message.receiver_id = receiver_id
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
