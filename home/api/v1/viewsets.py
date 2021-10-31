from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
    AppSerializer,
    PlanSerializer,
)
from home.models import App, Plan
from home.api.utils.api_utils import app_exists


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class AppViewSet(ViewSet):
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated,]

    @swagger_auto_schema(responses = {200: AppSerializer(many=True)})
    def list(self, request):
        queryset = App.objects.filter(user=request.user.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(request_body=AppSerializer)
    def create(self, request):
        data = request.data
        exists = app_exists(data=data, user=request.user)
        if exists:
            return Response({
                "detail": f"App with name {data['name']} exists",
                "message": "failed"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_201_CREATED
        )
    
    @swagger_auto_schema(responses = {200: AppSerializer()})
    def retrieve(self, request, pk=None):
        try:
            app = App.objects.get(user=request.user.id, pk=pk)
        except App.DoesNotExist:
            return Response({
                "data": "App not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(app)
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )
    
    @swagger_auto_schema(request_body=AppSerializer)
    def update(self, request, pk=None):
        try:
            app = App.objects.get(user=request.user.id, pk=pk)
        except App.DoesNotExist:
            return Response({
                "data": "App not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        data = request.data
        exists = app_exists(data=data, user=request.user)
        if exists:
            return Response({
                "detail": f"App with name {data['name']} exists",
                "message": "failed"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.serializer_class(app, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )
    
    @swagger_auto_schema(request_body=AppSerializer)
    def partial_update(self, request, pk=None):
        try:
            app = App.objects.get(user=request.user.id, pk=pk)
        except App.DoesNotExist:
            return Response({
                "data": "App not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(app, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(request_body=AppSerializer)
    def destroy(self, request, pk=None):
        try:
            app = App.objects.get(user=request.user.id, pk=pk)
        except App.DoesNotExist:
            return Response({
                "data": "App not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        app.delete()
        return Response({
            "message": "success"
            },
            status=status.HTTP_200_OK
        )


class PlanViewSet(ViewSet):
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated,]

    @swagger_auto_schema(responses = {200: PlanSerializer(many=True)})
    def list(self, request):
        queryset = Plan.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )
    
    @swagger_auto_schema(responses = {200: PlanSerializer()})
    def retrieve(self, request, pk=None):
        try:
            plan = Plan.objects.get(pk=pk)
        except Plan.DoesNotExist:
            return Response({
                "data": "Plan not found",
                "message": "failed"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(plan)
        return Response({
            "data": serializer.data,
            "message": "success"
            },
            status=status.HTTP_200_OK
        )

