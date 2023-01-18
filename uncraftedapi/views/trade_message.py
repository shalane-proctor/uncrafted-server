from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from uncraftedapi.models import TradeMessage, Message, Trade


class TradeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeMessage
        fields = ('id', 'post_id', 'reaction_id', 'user_id')
        depth = 0
class TradeMessageView(ViewSet):
  
    def retrieve(self, request, pk):
        trade_message = TradeMessage.objects.get(pk=pk)
        serializer = TradeMessageSerializer(trade_message)
        return Response(serializer.data)

    def list(self, request):
        trade_messages = TradeMessage.objects.all()
        message = request.query_params.get('message', None)
        if message is not None:
            trade_messages = trade_messages.filter(message_id=message)
        trade = request.query_params.get('trade', None)
        if trade is not None:
            trade_messages = trade_messages.filter(trade_id=trade)
        serializer = TradeMessageSerializer(trade_messages, many=True)
        return Response(serializer.data)

    def create(self, request):
        message = Message.objects.get(message_id=request.data["message"])
        trade = Trade.objects.get(trade=request.data["trade"])
        trade_message = TradeMessage.objects.create(
            message=message,
            trade=trade,
        )
        serializer = TradeMessageSerializer(trade_message)
        return Response(serializer.data)

    def update(self, request, pk):

        post = Post.objects.get(pk=pk)
        user = User.objects.get(uid=request.data["user"]),
        post.owner_profile_id = user,
        post.item_name = request.data["item_name"],
        post.color = request.data["color"],
        post.amount = request.data["amount"],
        post.image_url = request.data["image_url"],
        post.trade_preference = request.data["trade_preference"],
        post.description = request.data["desription"],
        post.is_draft = request.data["is_draft"],
        post.is_pending = request.data["is_pending"],
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
