from django.shortcuts import render, HttpResponse
from .form import CustomUserForm
from django.http import JsonResponse
from .models import CustomUser

def main(request):
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

# debugging
def users_list(request):
    data = list(CustomUser.objects.values('username', 'email', 'contact', 'role'))
    return JsonResponse(data, safe=False)
