from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
import sweetify


def registration(request):
    """Return the registration.html file"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password1']
            )

            if user:
                auth.login(user=user, request=request)
                sweetify.success(
                    request, "You have successfully registered!",
                    icon="success"
                )
                return redirect(reverse('index'))

            else:
                sweetify.error(
                    request,
                    """We're truly sorry. We are unable
                    to register your account at this time.""",
                    icon="error"
                )

    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {
        "registration_form": registration_form})


def login(request):
    """Return the login.html file"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)

                sweetify.sweetalert(
                    request,
                    """You have successfully logged in!""",
                    icon="success"
                )
                return redirect(reverse('index'))

            else:
                login_form.add_error(
                    None,
                    "Your username or password is incorrect"
                )

    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {"login_form": login_form})


def userprofile(request):
    """Return the profile.html file"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})


@login_required
def logout(request):
    """Logs out the user"""
    auth.logout(request)
    sweetify.sweetalert(
        request, "You have successfully been logged out!",
        icon="success"
    )
    return redirect(reverse('index'))
