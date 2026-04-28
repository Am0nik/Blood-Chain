from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import logout

User = get_user_model()
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Registration successful.")
            return redirect('index') 
        else:
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email') 
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back!")
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('index') 
        else:
            messages.error(request, "Invalid email or password.")
            
    return render(request, 'login.html')

@login_required
def profile_view(request):

    return render(request, 'profile.html')

@login_required
def settings_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'settings.html', {'form': form})

from django.core.paginator import Paginator
@login_required
def my_donations_view(request):
    # 1. Данные для основной таблицы (с пагинацией)
    donations_list = request.user.my_donations.all().order_by('-date')
    paginator = Paginator(donations_list, 10) 
    page_number = request.GET.get('page')
    donations_obj = paginator.get_page(page_number)
    user_donations = list(request.user.my_donations.all().order_by('-date')[:7])
    first_date = None
    last_date = None
    if user_donations:
        max_am = max(d.amount for d in user_donations) or 450
        for donation in user_donations:
            donation.bar_height = (donation.amount / max_am) * 100
        
        first_date = user_donations[-1].date 
        last_date = user_donations[0].date
    
    context = {
        'donations': donations_obj, 
        'history': user_donations,
        'first_date': first_date,
        'last_date': last_date
    }
    
    return render(request, 'my_donations.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('index')

def terms_and_conditions_view(request):
    return render(request, 'termsandconditions.html')