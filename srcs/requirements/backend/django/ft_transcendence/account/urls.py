from django.urls import path
from .views import UserRegisterView, LoginView, LogoutView, ProfileView, AllUserView, UserView, getProfileView, AvatarView, UpdateAvatarView, SendOTPView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'account'

urlpatterns = [
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('register/', UserRegisterView.as_view(), name='register'),
	path('profile/', ProfileView.as_view(), name='profile'),
	path('profile/<str:username>/', getProfileView.as_view(), name='user-profile'),
	path('', AllUserView.as_view(), name='account'),
	path('<int:pk>/', UserView.as_view(), name='account-nunero'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('profile/avatar/<str:avatar>/', AvatarView.as_view(), name='get-avatar'),
	path('profile/avatar/', UpdateAvatarView.as_view(), name='avatar'),
	path('otp/', SendOTPView.as_view(), name='otp'),
]