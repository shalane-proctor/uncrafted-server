"""uncrafted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from uncraftedapi.views import UserView, PostView, TradeView, MessageView, TradeMessageView
from rest_framework import routers
from uncraftedapi.views import check_user, register_user
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserView, 'user')
router.register(r'post', PostView, 'post')
router.register(r'trade', TradeView, 'trade')
router.register(r'message', MessageView, 'message')
router.register(r'trademessage', TradeMessageView, 'trademessage')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('post-comments/<int:post_id>/', PostCommentView.as_view(), name='posts')
]
