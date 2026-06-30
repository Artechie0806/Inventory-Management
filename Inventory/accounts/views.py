from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class RoleBasedLoginView(LoginView):
    # 1. Point Django to your custom HTML file
    template_name = 'accounts/login.html'
    
    # 2. Prevent logged-in users from seeing the login page again
    redirect_authenticated_user = True 

    # 3. Route the user based on their specific role
    def get_success_url(self):
        user = self.request.user
        
        if user.role == 'CASHIER':
            return reverse_lazy('billing:pos_dashboard') # Assuming you name your URLs
            
        elif user.role == 'VENDOR':
            return reverse_lazy('stock:vendor_portal')
            
        elif user.role == 'MANAGER':
            return reverse_lazy('stock:manager_dashboard')
            
        elif user.role == 'CUSTOMER':
            return reverse_lazy('e_commerce:storefront')
            
        # Fallback if no specific role matches
        return reverse_lazy('home')