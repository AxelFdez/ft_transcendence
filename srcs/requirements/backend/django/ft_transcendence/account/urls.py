from django.urls import path
from .views import UserViewSet, LoginView

app_name = 'account'

urlpatterns = [
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', UserViewSet.logout, name='logout'),
	path('register/', UserViewSet.as_view({'post': 'register'}), name='register'),
	path('profile/', UserViewSet.profile, name='profile'),
	path('', UserViewSet.as_view({'get': 'list'}), name='list'),
]