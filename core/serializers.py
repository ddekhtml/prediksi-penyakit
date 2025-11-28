from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import MedicalRecord


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"
        read_only_fields = ["created_at", "diagnosis"]

    # def create(self, validated_data):
    #     # ambil user dari request context
    #     user = self.context['request'].user
    #     validated_data["patient"] = user
    #     return super().create(validated_data)
class UserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name", "phonenumber"]


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'phonenumber']
