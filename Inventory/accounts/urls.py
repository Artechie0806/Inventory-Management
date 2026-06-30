# accounts/urls.py
from django.urls import path
from .views import RoleBasedLoginView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    # Point the login URL to your custom view
    path('login/', RoleBasedLoginView.as_view(), name='login'),
    
    # You can use Django's default logout view, just tell it where to go next
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
]