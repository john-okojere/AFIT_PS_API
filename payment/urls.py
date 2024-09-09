from django.urls import path
from .views import PaymentViewSet, AdminViewSet, get_wallet_address, get_admin_wallet_address, get_fee_amount
from  . import views
from .views import DepartmentListView, LevelListView, FeeAmountView
from .views import LoginView, RegisterView, LogoutView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('admins/', AdminViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('admin/wallet/', get_wallet_address),
    path('get_admin_wallet_address/', get_admin_wallet_address),  # New endpoint
    path('populate/', views.populate ),
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:department_id>/levels/', LevelListView.as_view(), name='level-list'),
    path('fees/<int:department_id>/<int:level>/', FeeAmountView.as_view(), name='fee-amount'),

    # Route for user login
    path('login/', LoginView.as_view(), name='login'),

    # Route for user registration
    path('register/', RegisterView.as_view(), name='register'),

    # Route for logging out (if applicable)
    path('logout/', LogoutView.as_view(), name='logout'),

    # Route for refreshing JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('save_payment/', views.save_payment, name='save_payment'),
     path('update_payment_status/<int:payment_id>/', views.update_payment_status, name='update_payment_status'),
]