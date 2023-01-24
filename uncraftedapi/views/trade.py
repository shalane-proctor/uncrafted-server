from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from uncraftedapi.models import Trade, Post
from rest_framework.decorators import action


class TradeSerializer(serializers.ModelSerializer):
    """JSON serializer for Trades
    """
    class Meta:
        model = Trade
        fields = ('id', 'item_wanted', 'item_offered', 'is_pending')
        depth = 2


class TradeView(ViewSet):

    def retrieve(self, request, pk):
        trade = Trade.objects.get(pk=pk)
        serializer = TradeSerializer(trade)
        return Response(serializer.data)

    def list(self, request):
        trades = Trade.objects.all()
        post = request.query_params.get('item_wanted', None)
        if post is not None:
            trades = trades.filter(post=post.id)
        post = request.query_params.get('item_offered', None)
        if post is not None:
            trades = trades.filter(post=post.id)
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)

    def create(self, request):
        item_wanted = Post.objects.get(pk=request.data["item_wanted"])
        item_offered = Post.objects.get(pk=request.data["item_offered"])
        trade = Trade.objects.create(
            item_wanted=item_wanted,
            item_offered=item_offered,
            is_pending=request.data["is_pending"],
        )
        serializer = TradeSerializer(trade)
        return Response(serializer.data)

    def update(self, request, pk):

        trade = Trade.objects.get(pk=pk)
        item_wanted = Post.objects.get(pk=request.data["item_wanted"])
        item_offered = Post.objects.get(pk=request.data["item_offered"])
        trade.item_wanted = item_wanted
        trade.item_offered = item_offered
        trade.is_pending = request.data["is_pending"]
        trade.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
