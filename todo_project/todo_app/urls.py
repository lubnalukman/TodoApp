from rest_framework .routers import DefaultRouter
from.views import TodoItemViewSet
from django.urls import path, include


router=DefaultRouter()
router.register(r'todos',TodoItemViewSet,basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    
]

