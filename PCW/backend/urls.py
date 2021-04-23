from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet
from . import views
from .views import SignUpView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    path('<str:room_name>/', views.room, name='room'),
]
