from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UpdateUserForm, UpdateProfileForm



def index(request):
    return render(request, 'index.html') #  вывод главной страницы


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'


class EmployeeForm:
    pass


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='news:news')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    if "Reset" in request.POST:  # если пользователь собирается удалить одно дело
        return render(request, 'profiles/profile.html')

    return render(request,
                  'profiles/profile.html', {
                      'user_form': user_form,
                      'profile_form': profile_form
                  })


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'profiles/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('accounts:users-profile')