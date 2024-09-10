from rest_framework import viewsets
from .models import Payment, Admin
from .serializers import PaymentSerializer, AdminSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from datetime import datetime
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

@api_view(['GET'])
def get_wallet_address(request):
    try:
        admin = Admin.objects.last()  # Get the most recent wallet address
        if admin:
            return Response({'wallet_address': admin.wallet_address}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No wallet address found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def get_admin_wallet_address(request):
    try:
        admin = Admin.objects.latest('id')  # Fetch the latest admin record
        data = {
            "addressTo": admin.wallet_address
        }
        return JsonResponse(data)
    except Admin.DoesNotExist:
        return JsonResponse({"error": "Admin wallet address not found"}, status=404)


@api_view(['POST'])
def save_payment(request):
    if request.method == 'POST':
        print(request.data)  # Debugging: print the incoming data
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()
            return Response({'payment_id': payment.id}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Debugging: print any validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_payment_status(request, payment_id):
    try:
        payment = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = PaymentSerializer(payment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department, Level

ETH_RATE = 10000  # 1 Ether = 10,000 NGN

@api_view(['GET'])
def get_fee_amount(request, department_name, level):
    try:
        department = Department.objects.get(name=department_name)
        level_instance = department.levels.get(level=level)
        fee_in_ngn = level_instance.fee_amount
        fee_in_eth = fee_in_ngn / ETH_RATE
        return Response({
            'department': department.name,
            'level': level,
            'fee_amount_ngn': fee_in_ngn,
            'fee_amount_eth': fee_in_eth
        })
    except Department.DoesNotExist:
        return Response({'error': 'Department not found'}, status=404)
    except Level.DoesNotExist:
        return Response({'error': 'Level not found'}, status=404)


from .fees import data as fees_data

def populate(request):
    for department_data in fees_data:
        department_name = department_data['department']
        department, created = Department.objects.get_or_create(name=department_name)

        for level_data in department_data['levels']:
            Level.objects.create(
                department=department,
                level=level_data['level'],
                fee_amount=level_data['fee_amount']
            )
    print("Database populated successfully")
    return JsonResponse({"ee":"wewe"})

from rest_framework import generics
from rest_framework.response import Response
from .serializers import DepartmentSerializer, LevelSerializer

class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class LevelListView(generics.ListAPIView):
    serializer_class = LevelSerializer

    def get_queryset(self):
        department_id = self.kwargs.get('department_id')
        department = Department.objects.get(id=department_id)
        return Level.objects.filter(department=department)

EXCHANGE_RATE = 3681359

def ngn_to_eth(amount_in_ngn, exchange_rate=EXCHANGE_RATE):
    """
    Convert NGN to ETH at a given exchange rate.
    
    :param amount_in_ngn: The amount in NGN to convert.
    :param exchange_rate: The rate of NGN to ETH conversion. Default is 10,000 NGN per ETH.
    :return: The equivalent amount in ETH.
    """
    return amount_in_ngn / exchange_rate

class FeeAmountView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        department_id = self.kwargs.get('department_id')
        level_number = self.kwargs.get('level')

        try:
            department = Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            level = Level.objects.get(department=department, level=level_number)
        except Level.DoesNotExist:
            return Response({'error': 'Level not found'}, status=status.HTTP_404_NOT_FOUND)

        fee_amount_ngn = level.fee_amount  # Assuming fee_amount is in NGN
        fee_amount_eth = ngn_to_eth(fee_amount_ngn)

        return Response({'amount_in_eth': fee_amount_eth, 'amount_in_ngn':fee_amount_ngn})
    

class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

from django.contrib.auth.models import User       
from django.contrib.auth import authenticate, login, logout

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            login(request, user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return Response({"detail": "User registered successfully"}, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "User logged out successfully"}, status=status.HTTP_200_OK)