from uncraftedapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):

    uid = request.data['uid']
    try:

        user = User.objects.get(uid=uid)
        data = {
            'id': user.id,
            'uid': user.uid,
            'username': user.username,
            'email': user.email,
            'about': user.about,
            'profile_image_url': user.profile_image_url,
            'instagram': user.instagram,
            'etsy': user.etsy,
        }
        return Response(data)
    except:
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    user = User.objects.create(
        uid=request.data['uid'],
        username=request.data['username'],
        email=request.data['email'],
        about=request.data['about'],
        profile_image_url=request.data['profile_image_url'],
        instagram=request.data['instagram'],
        etsy=request.data['etsy'],
    )

    data = {
        'id': user.id,
        'uid': user.uid,
        'username': user.username,
        'email': user.email,
        'about': user.about,
        'profile_image_url': user.profile_image_url,
        'instagram': user.instagram,
        'etsy': user.etsy,
    }
    return Response(data)
