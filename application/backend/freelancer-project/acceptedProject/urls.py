
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('create', views.AcceptedProjectViewSet)
router.register('milestone', views.AcceptedMilestoneViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('accept', views.acceptProject),
]
