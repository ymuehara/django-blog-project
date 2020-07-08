from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # saves the user
            # validated form data will be in form.cleaned_data dictionary and this will have been converted into python type from the form
            username = form.cleaned_data.get('username')
            # flash message. After need to update template to show the message
            messages.success(
                request, f'{username} your account has been created! You are now able to login')
            # blog-hoome is the name we gave to our url pattern on the blog homepage
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        # resquest.POST passes the post data. Current logged in user. The instance will populate the form with current user info
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # The instance will populate the form with current user info
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Yay! {request.user} your account has been updated!')
            # causes the browser to send a GET request and we don't send another POST request if we reload the page
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
