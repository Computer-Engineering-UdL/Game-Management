from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from Accounts.forms import SignUpForm
from GameManagement.settings import SIGNUP_REDIRECT_URL


def signup(request):
    """Sign up a new user."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signing up
            messages.success(request, 'Account created successfully!')
            return redirect(SIGNUP_REDIRECT_URL)
        else:
            messages.error(request, 'Invalid data. Please try again')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
