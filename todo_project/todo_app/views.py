from rest_framework import viewsets, permissions,generics, serializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import TodoItem
from rest_framework.views import APIView
from .serializers import TodoItemSerializer,RegisterSerializer,LoginSerializer,UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset=TodoItem.objects.all()
    '''permission_classes = [IsAuthenticated]



    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)'''

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class=LoginSerializer
    def post(self, request, *args, **kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)

        if user is not None:
            refresh=RefreshToken.for_user(user)
            user_serializer=UserSerializer()
            return Response({
                'refresh':str(refresh),
                'access': str(refresh.access_token),
                'user' :user_serializer.data 
            })
        
        return Response({'detail':'invalid credentials'},status=401)

class DashboardView(APIView):
    permission_classes=(IsAuthenticated)
    def get(self,request):
        user=request.user
        user_serializer=UserSerializer(user)
        return Response({
            'message':'welcome to dashboard',
            'user':user_serializer.data
        },status=200)
