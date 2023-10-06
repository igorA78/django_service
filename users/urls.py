from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, register_begin, register_end, \
                        UserListView, UserDetailView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register_begin/', register_begin, name='register_begin'),
    path('register_end/', register_end, name='register_end'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('list/', UserListView.as_view(), name='list'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='detail'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update'),
]
