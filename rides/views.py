from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Ride, RideEvent
from django import forms
from django.contrib import messages


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['pickup_location', 'destination', 'price']


class CreateRideView(LoginRequiredMixin, generic.CreateView):
    model = Ride
    form_class = RideForm
    template_name = 'rides/ride_form.html'

    def form_valid(self, form):
        ride = form.save(commit=False)
        ride.customer = self.request.user
        # total_distance generated in model.save()
        # validate customer balance
        if ride.price > self.request.user.balance:
            form.add_error('price', 'Price exceeds your balance')
            return self.form_invalid(form)
        ride.save()
        messages.success(self.request, 'Ride created')
        return redirect('rides:ride_detail', pk=ride.pk)


class RideListView(LoginRequiredMixin, generic.ListView):
    model = Ride
    template_name = 'rides/ride_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.user_role == 'rider':
            return Ride.objects.filter(status='created')
        return Ride.objects.filter(customer=user)


class RideDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ride
    template_name = 'rides/ride_detail.html'


class RideUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ride
    fields = ['pickup_location', 'destination', 'price', 'status']
    template_name = 'rides/ride_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Only allow editing if no rider is assigned or if rider is current user
        if self.object.rider and self.object.rider != request.user and request.user.user_role != 'staff':
            return redirect('rides:ride_detail', pk=self.object.pk)
        return super().dispatch(request, *args, **kwargs)


class RideDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ride
    success_url = reverse_lazy('home')
    template_name = 'rides/ride_confirm_delete.html'


class CreateRideEventView(LoginRequiredMixin, generic.CreateView):
    model = RideEvent
    fields = ['description']
    template_name = 'rides/rideevent_form.html'

    def form_valid(self, form):
        ride = get_object_or_404(Ride, pk=self.kwargs.get('ride_pk'))
        last = ride.events.order_by('-step_count').first()
        next_step = (last.step_count + 1) if last else 1
        event = form.save(commit=False)
        event.ride = ride
        event.step_count = next_step
        event.save()
        return redirect('rides:ride_detail', pk=ride.pk)
