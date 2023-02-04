from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from uncraftedapi.models import TradeMessage, Message, Trade
from rest_framework import generics


class TradeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeMessage
        fields = ('id', 'message', 'trade')
        depth = 2
class TradeMessageView(ViewSet):
  
    def retrieve(self, request, pk):
        trade_message = TradeMessage.objects.get(pk=pk)
        serializer = TradeMessageSerializer(trade_message)
        return Response(serializer.data)

    def list(self, request):
        trade_messages = TradeMessage.objects.all()
        message = request.query_params.get('message', None)
        if message is not None:
            message = trade_messages.filter(message=message.id)
        trade = request.query_params.get('trade', None)
        if trade is not None:
            trade = trade_messages.filter(trade=trade.id)
        serializer = TradeMessageSerializer(trade_messages, many=True)
        return Response(serializer.data)

    def create(self, request):
        message = Message.objects.get(pk=request.data["message"])
        trade = Trade.objects.get(pk=request.data["trade"])
        trade_message = TradeMessage.objects.create(
            message=message,
            trade=trade,
        )
        serializer = TradeMessageSerializer(trade_message)
        return Response(serializer.data)

    def update(self, request, pk):
        trade_message = TradeMessage.objects.get(pk=pk)
        message = Message.objects.get(pk=request.data["message"])
        trade = Trade.objects.get(pk=request.data["trade"])
        trade_message.message = message
        trade_message.trade = trade
        trade_message.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        trade_message = TradeMessage.objects.get(pk=pk)
        trade_message.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserTradeMessageView(generics.ListCreateAPIView):
  serializer_class = TradeMessageSerializer

  def get_queryset(self):
    sender_id = self.kwargs['sender_id']
    return Message.objects.filter(trade__sender__id=sender_id)

class ByTradeTradeMessageView(generics.ListCreateAPIView):
  serializer_class = TradeMessageSerializer

  def get_queryset(self):
    trade_id = self.kwargs['trade_id']
    return TradeMessage.objects.filter(trade__id=trade_id)
