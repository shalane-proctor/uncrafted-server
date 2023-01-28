from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from uncraftedapi.models import User
from rest_framework import generics

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ('id', 'uid', 'username', 'favorite_craft', 'email', 'about',
                'profile_image_url', 'instagram', 'etsy')
class UserView(ViewSet):
    def retrieve(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.create(
            uid=request.data["uid"],
            username=request.data["username"],
            favorite_craft=request.data["favorite_craft"],
            email=request.data["email"],
            about=request.data["about"],
            profile_image_url=request.data["profile_image_url"],
            instagram=request.data["instagram"],
            etsy=request.data["etsy"],
        )
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = User.objects.get(pk=pk)
        user.username = request.data["username"]
        user.favorite_craft = request.data["favorite_craft"]
        user.email = request.data["email"]
        user.about = request.data["about"]
        user.profile_image_url = request.data["profile_image_url"]
        user.instagram = request.data["instagram"]
        user.etsy = request.data["etsy"]
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserByUidView(generics.ListCreateAPIView):
  serializer_class = UserSerializer

  def get_queryset(self):
    uid = self.kwargs['uid']
    return User.objects.filter(uid=uid)
