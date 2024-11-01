from rest_framework import serializers
from .models import TodoItem
from django.contrib.auth.models import User 

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'description', 'due_date', 'completed', 'created', 'updated', 'user']
        read_only_fields = ['created', 'updated', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id','username','email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['username','email','password']

    def create(self,validated_data):
        user=User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])
        return user
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)