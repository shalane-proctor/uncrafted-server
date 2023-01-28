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
from uncraftedapi.views import UserView, PostView, TradeView, MessageView, TradeMessageView, UserPostView, UserMessageView, PostTradeView, TradeRequestsView, UserOfferedTradeView, UserTradeMessageView, UserByUidView
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
    path('trade-post/<int:item_offered_id>/',
         PostTradeView.as_view(), name='posts'),
    
    path('trade-wanted/<int:item_wanted_id>/',
         TradeRequestsView.as_view(), name='item_wanted'),
    
    path('trade-user/<int:trade_by_user_id>/',
         UserOfferedTradeView.as_view(), name='trade_by_user'),
    
    path('post-user/<int:owner_profile_id>/',
         UserPostView.as_view(), name='user'),
    
    path('message-user/<int:sender_id>/',
         UserMessageView.as_view(), name='user'),
    
    path('trademessage-trade/<int:trade_id>/',
         UserTradeMessageView.as_view(), name='trade'),
    
    path('user-uid/<str:uid>/',
         UserByUidView.as_view(), name='uid'),
]
