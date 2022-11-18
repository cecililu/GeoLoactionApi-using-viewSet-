from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('geoapi', views.GeoViewSet,basename='geoapi')
router.register('user', views.UserViewSet,basename='user')


# user_list=views.UserViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('v1/',include(router.urls)),
]