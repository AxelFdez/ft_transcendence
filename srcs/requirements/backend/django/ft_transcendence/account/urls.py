from django.urls import path
from .views import UserViewSet, LoginView, LogoutView, ProfileView

app_name = 'account'

urlpatterns = [
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('register/', UserViewSet.as_view({'post': 'register'}), name='register'),
	path('profile/', ProfileView.as_view(), name='profile'),
	path('', ProfileView.as_view(), name='account'),
]