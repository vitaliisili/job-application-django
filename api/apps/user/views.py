from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from apps.core.utils import JwtToken, Validate
from apps.user.filters import UserFilter
from apps.user.permissions import UserPermission
from apps.user.serializers import BaseUserSerializer, RegisterUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for managing user accounts."""

    queryset = get_user_model().objects.all()
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = (UserPermission,)
    search_fields = ['$name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    filterset_class = UserFilter

    def create(self, request, *args, **kwargs):
        """Creates a new user account."""

        password = request.data.get('password')
        Validate.password_validation(password)

        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(JwtToken.get_jwt_token(user), status=status.HTTP_201_CREATED)

    @action(detail=False)
    def me(self, request):
        """Retrieves the current user's account details."""

        user_serializer = BaseUserSerializer(request.user)
        return Response(user_serializer.data, status=200)
