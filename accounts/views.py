from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')  # Replace 'login' with the name of your login URL pattern
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
