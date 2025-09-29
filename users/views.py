from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
from datetime import timedelta
from .models import CustomUser, OTP
from .forms import RegistrationForm, UpdateProfileForm  # Import the new form
from orders.models import Order  # Import Order model
from django.contrib.auth.decorators import login_required
import smtplib
import random

# Email setup (example using Gmail)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password'

def send_email(recipient, code):
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        subject = "Your OTP Code"
        message = f"Subject: {subject}\n\nYour OTP is {code}"
        server.sendmail(EMAIL_HOST_USER, recipient, message)
        server.quit()
    except Exception as e:
        print("Email sending failed:", e)

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.set_password(form.cleaned_data['password'])
            user.is_active = False  # Activate after OTP verification
            user.save()
            
            # Generate OTP
            otp_code = OTP.generate_otp()
            otp_expiry = timezone.now() + timedelta(minutes=5)
            OTP.objects.create(user=user, code=otp_code, expires_at=otp_expiry)
            
            # Instead of sending email, just print OTP to console
            print(f"OTP for {user.email} is: {otp_code}")
            
            request.session['email'] = user.email
            return redirect('verify_otp')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# OTP verification
def verify_otp_view(request):
    email = request.session.get('email')
    if not email:
        return redirect('register')
    
    user = CustomUser.objects.get(email=email)
    if request.method == 'POST':
        code = request.POST.get('otp')
        try:
            otp_obj = OTP.objects.filter(user=user, code=code).latest('created_at')
            if otp_obj.is_expired():
                message = "OTP expired"
            else:
                user.is_active = True
                user.save()
                login(request, user)
                message = "Email verified! Logged in."
                return redirect('home')
        except OTP.DoesNotExist:
            message = "Invalid OTP"
        return render(request, 'users/verify_otp.html', {'message': message})
    return render(request, 'users/verify_otp.html')
    
# Login
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            message = "Invalid credentials"
            return render(request, 'users/login.html', {'message': message})
    return render(request, 'users/login.html')

# Home
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'users/home.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('users:login')  # Updated here


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')  # Redirect to profile after update
    else:
        form = UpdateProfileForm(instance=request.user)
    
    # Fetch user's orders
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product').order_by('-created_at')
    
    return render(request, 'users/profile.html', {
        'form': form,
        'orders': orders,
    })