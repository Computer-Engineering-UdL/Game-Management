from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseBadRequest
from Accounts.forms import SignUpForm
from GameManagement.settings import SIGNUP_REDIRECT_URL


def signup(request):
    """Sign up a new user."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect(SIGNUP_REDIRECT_URL)
        else:
            messages.error(request, 'Error creating your account.')
            return HttpResponseBadRequest('Error creating your account.')
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
