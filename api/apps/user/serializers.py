from django.contrib.auth import get_user_model
from rest_framework import serializers


class BaseUserSerializer(serializers.ModelSerializer):
    """Base serializer for user models.
    Attributes:
        image (ImageField): The profile image of the user. Not required.
    Meta:
        model: The user model to be serialized.
        fields: The fields to be included in the serialized representation.
        read_only_fields: The fields that are read-only and cannot be modified.
    Methods:
        create: Creates and returns a new user instance.
    """

    image = serializers.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name', 'image', 'is_verified']
        read_only_fields = ['id', 'created_at', 'updated_at']


class RegisterUserSerializer(BaseUserSerializer):
    """Serializer for registering new users.
    Meta:
        model: The user model to be serialized.
        fields: The fields to be included in the serialized representation.
    """

    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'password']
