# pocketsense_project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'pocketsense',  # Custom app
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# pocketsense/models.py
from django.contrib.auth.models import User
from django.db import models

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_by')

class Expense(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='expenses')

class Payment(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payer')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# pocketsense/serializers.py
from rest_framework import serializers
from .models import Expense, Payment, Friend
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

# pocketsense/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Expense, Payment, Friend
from .serializers import ExpenseSerializer, PaymentSerializer, FriendSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

# pocketsense/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, PaymentViewSet, FriendViewSet

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'friends', FriendViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
