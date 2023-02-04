from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from uncraftedapi.models import Trade, Post, User
from rest_framework.decorators import action
from rest_framework import generics

class TradeSerializer(serializers.ModelSerializer):
    """JSON serializer for Trades
    """
    class Meta:
        model = Trade
        fields = ('id', 'trade_by_user', 'item_wanted', 'item_offered', 'is_pending')
        depth = 2


class TradeView(ViewSet):

    def retrieve(self, request, pk):
        trade = Trade.objects.get(pk=pk)
        serializer = TradeSerializer(trade)
        return Response(serializer.data)

    def list(self, request):
        trades = Trade.objects.all()
        user = request.query_params.get('trade_by_user', None)
        if user is not None:
            trades = trades.filter(uid=user.uid)
        post = request.query_params.get('item_wanted', None)
        if post is not None:
            trades = trades.filter(post=post.id)
        post = request.query_params.get('item_offered', None)
        if post is not None:
            trades = trades.filter(post=post.id)
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)

    def create(self, request):
        trade_by_user = User.objects.get(pk=request.data["trade_by_user"])
        item_wanted = Post.objects.get(pk=request.data["item_wanted"])
        item_offered = Post.objects.get(pk=request.data["item_offered"])
        trade = Trade.objects.create(
            trade_by_user=trade_by_user,
            item_wanted=item_wanted,
            item_offered=item_offered,
            is_pending=request.data["is_pending"],
        )
        serializer = TradeSerializer(trade)
        return Response(serializer.data)

    def update(self, request, pk):

        trade = Trade.objects.get(pk=pk)
        trade_by_user = User.objects.get(uid=request.data["trade_by_user"])
        item_wanted = Post.objects.get(pk=request.data["item_wanted"])
        item_offered = Post.objects.get(pk=request.data["item_offered"])
        trade.trade_by_user = trade_by_user
        trade.item_wanted = item_wanted
        trade.item_offered = item_offered
        
        trade.is_pending = request.data["is_pending"]
        trade.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        trade = Trade.objects.get(pk=pk)
        trade.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserOfferedTradeView(generics.ListCreateAPIView):
  serializer_class = TradeSerializer

  def get_queryset(self):
    trade_by_user_id = self.kwargs['trade_by_user_id']
    return Trade.objects.filter(trade_by_user__id=trade_by_user_id)


class TradeRequestsView(generics.ListCreateAPIView):
  serializer_class = TradeSerializer

  def get_queryset(self):
    item_wanted_id = self.kwargs['item_wanted_id']
    return Trade.objects.filter(item_wanted__id=item_wanted_id)

class PostTradeView(generics.ListCreateAPIView):
  serializer_class = TradeSerializer

  def get_queryset(self):
    item_offered_id = self.kwargs['item_offered_id']
    return Trade.objects.filter(item_offered__id=item_offered_id)
