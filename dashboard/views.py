from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django import forms
from accounts.models import CustomUser
from django.contrib import messages
from rides.models import Ride


def staff_required(view_func):
    decorated = login_required(user_passes_test(lambda u: u.user_role == 'staff')(view_func))
    return decorated


@staff_required
def dashboard_home(request):
    return render(request, 'dashboard/home.html')


class AddBalanceForm(forms.Form):
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    amount = forms.DecimalField(max_digits=10, decimal_places=2)


@staff_required
def add_balance(request):
    if request.method == 'POST':
        form = AddBalanceForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            amount = form.cleaned_data['amount']
            user.balance += amount
            user.save()
            messages.success(request, f'Added {amount} to {user.username}')
            return redirect('dashboard:home')
    else:
        form = AddBalanceForm()
    return render(request, 'dashboard/add_balance.html', {'form': form})


@staff_required
def users_list(request):
    users = CustomUser.objects.all()
    return render(request, 'dashboard/users_list.html', {'users': users})


@staff_required
def rides_list(request):
    rides = Ride.objects.all()
    return render(request, 'dashboard/rides_list.html', {'rides': rides})
