from django.urls import path
from .views import home, handleSignUp, handleLogin, handleLogout

urlpatterns = [
    path('', home, name = 'home'),
    path('signup/', handleSignUp, name = 'handleSignUp'),
    path('login/', handleLogin, name = 'handleLogin'),
    path('logout/', handleLogout, name = 'handleLogout'),
]