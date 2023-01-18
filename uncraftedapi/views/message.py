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
        depth = 2


class MessageView(ViewSet):

    def retrieve(self, request, pk):
        message = Message.objects.get(pk=pk)
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    def list(self, request):
        messages = Message.objects.all()
        user = request.query_params.get('sender', None)
        if user is not None:
            messages = messages.filter(uid=user.uid)
        user = request.query_params.get('receiver', None)
        if user is not None:
            messages = messages.filter(uid=user.uid)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(uid=request.data["user"])
        user = User.objects.get(uid=request.data["user"])
        message = Message.objects.create(
            sender=user,
            receiver=user,
            subject=request.data["subject"],
            message_content=request.data["message_content"],
            is_new=request.data["is_new"],
            connected_to_trade=request.data["connected_to_trade"],
        )
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    def update(self, request, pk):

        message = message.objects.get(pk=pk)
        user = User.objects.get(uid=request.data["user"]),
        message.sender = user,
        message.receiver = user,
        message.subject = request.data["subject"],
        message.message_content = request.data["message_content"],
        message.is_new = request.data["is_new"],
        message.connected_to_trade = request.data["connected_to_trade"],
        message.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        message = Message.objects.get(pk=pk)
        message.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
