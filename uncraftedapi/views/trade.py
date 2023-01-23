from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from uncraftedapi.models import Trade, User, Post
from rest_framework.decorators import action


class TradeSerializer(serializers.ModelSerializer):
    """JSON serializer for Trades
    """
    class Meta:
        model = Trade
        fields = ('id', 'user_of_wanted', 'user_of_offered',
                  'item_wanted', 'item_offered', 'is_pending')
        depth = 2


class TradeView(ViewSet):

    def retrieve(self, request, pk):
        trade = Trade.objects.get(pk=pk)
        serializer = TradeSerializer(trade)
        return Response(serializer.data)

    def list(self, request):
        trades = Trade.objects.all()
        user = request.query_params.get('user_of_wanted', None)
        if user is not None:
            trades = trades.filter(uid=user.uid)
        user = request.query_params.get('user_of_offered', None)
        if user is not None:
            trades = trades.filter(uid=user.uid)
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)

    def create(self, request):
        user_of_wanted = User.objects.get(uid=request.data["user_of_wanted"])
        user_of_offered = User.objects.get(uid=request.data["user_of_offered"])
        item_wanted = Post.objects.get(pk=request.data["item_wanted"])
        item_offered = Post.objects.get(pk=request.data["item_offered"])
        trade = Trade.objects.create(
            user_of_wanted=user_of_wanted,
            user_of_offered=user_of_offered,
            item_wanted=item_wanted,
            item_offered=item_offered,
            is_pending=request.data["is_pending"],
        )
        serializer = TradeSerializer(trade)
        return Response(serializer.data)

    def update(self, request, pk):

        trade = Trade.objects.get(pk=pk)
        user_of_wanted = User.objects.get(uid=request.data["user_of_wanted"])
        user_of_offered = User.objects.get(uid=request.data["user_of_offered"])
        item_wanted = Post.objects.get(pk=request.data["item_wanted"])
        item_offered = Post.objects.get(pk=request.data["item_offered"])
        trade.user_of_wanted = user_of_wanted,
        trade.user_of_offered = user_of_offered,
        trade.item_wanted = item_wanted,
        trade.item_offered = item_offered,
        trade.is_pending = request.data["is_pending"],
        trade.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
