from django.shortcuts import render, HttpResponse, redirect
from .form import CustomUserForm, BasicUserDetailsForm
from django.http import JsonResponse
from .models import CustomUser, BasicUserDetails
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponse(f"User Created: {user.username} ({user.first_name})")
        else:
            return HttpResponse(f"<h3>Form is invalid:</h3> {form.errors.as_ul()}")
    else:
        form = CustomUserForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

@login_required
def user_details(request):
    if request.method == 'POST':
        user = request.user
        form = BasicUserDetailsForm(request.POST)
        if form.is_valid():
            form.instance.user = user
            form.save()
            return HttpResponse(list(BasicUserDetails.objects.all().values()))
    else:
        form = BasicUserDetailsForm()
    return render(request, 'user_details.html', {'form': form})
    # user = request.user
    # return HttpResponse(CustomUser.objects.get(username=user.username).contact)

# debugging
def users_list(request):
    data = list(CustomUser.objects.values('username', 'email', 'contact', 'role'))
    return JsonResponse(data, safe=False)
