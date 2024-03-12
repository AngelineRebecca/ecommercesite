from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin = authenticate(request, username=username, password=password)
        if admin is not None:
            login(request, admin)
            return redirect('admin_dashboard')
        else:
            # Handle invalid credentials
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'})
    return render(request, 'admin_login.html')

def user_login(request):
    return render(request, 'user_login.html')
def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')  # Redirect to user dashboard upon successful login
        else:
            # Handle invalid login
            return render(request, 'user_login.html', {'error_message': 'Invalid email or password'})
    else:
        return render(request, 'user_login.html')
    
def admin_dashboard(request):
    # Retrieve all registered users from the database
    registered_users = user_login.objects.all()
    
    # Pass the registered users to the template for rendering
    return render(request, 'admin_dashboard.html', {'registered_users': registered_users})    

def index(request):
    # Your view logic goes here
    return render(request, 'admin_login/index.html')