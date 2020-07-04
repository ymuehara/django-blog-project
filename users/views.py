from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # saves the user
            # validated form data will be in form.cleaned_data dictionary and this will have been converted into python type from the form
            username = form.cleaned_data.get('username')
            # flash message. After need to update template to show the message
            messages.success(request, f'Account created for {username}!')
            # blog-hoome is the name we gave to our url pattern on the blog homepage
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
