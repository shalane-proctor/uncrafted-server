from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from uncraftedapi.models import Post, User
from rest_framework.decorators import action


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Post
        fields = ('id', 'posted_by_user', 'owner_profile_id', 'item_name',
                  'color', 'amount', 'image_url', 'trade_preference', 'description', 'is_draft', 'is_pending')
        depth = 2


class PostView(ViewSet):

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        posts = Post.objects.all()
        user = request.query_params.get('posted_by_user', None)
        if user is not None:
            posts = posts.filter(uid=user.uid)
        user = request.query_params.get('owner_profile_id', None)
        if user is not None:
            posts = posts.filter(uid=user.uid)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(uid=request.data["user"])
        user = User.objects.get(uid=request.data["user"])
        post = Post.objects.create(
            posted_by_user=user,
            owner_profile_id=user,
            item_name=request.data["item_name"],
            color=request.data["color"],
            amount=request.data["amount"],
            image_url=request.data["image_url"],
            trade_preference=request.data["trade_preference"],
            description=request.data["desription"],
            is_draft=request.data["is_draft"],
            is_pending=request.data["is_pending"],
        )
        serializer = PostSerializer(post)
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
