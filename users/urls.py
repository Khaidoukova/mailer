from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, verify_email, UsersListView, UserDetailView, UserUpdateView, \
    UserMailConfirmView

app_name = UsersConfig.name
urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('confirm_email', UserMailConfirmView.as_view(), name='confirm_email'),
    path('verify/<str:key>/', verify_email, name='verify_email'),
    path('users_list/', UsersListView.as_view(), name='users_list'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='user_update')
]
