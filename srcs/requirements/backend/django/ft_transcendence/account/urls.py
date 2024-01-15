from django.urls import path
from .views import UserRegisterView, LoginView, LogoutView, ProfileView, AllUserView, UserView, getProfileView

app_name = 'account'

urlpatterns = [
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('register/', UserRegisterView.as_view(), name='register'),
	path('profile/', ProfileView.as_view(), name='profile'),
	path('profile/<str:username>/', getProfileView.as_view(), name='user-profile'),
	path('', AllUserView.as_view(), name='account'),
	path('<int:pk>/', UserView.as_view(), name='account-nunero'),
]