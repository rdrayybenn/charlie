from django.urls import path
from . import views

app_name = 'rides'

urlpatterns = [
    path('', views.RideListView.as_view(), name='ride_list'),
    path('create/', views.CreateRideView.as_view(), name='ride_create'),
    path('<int:pk>/', views.RideDetailView.as_view(), name='ride_detail'),
    path('<int:pk>/edit/', views.RideUpdateView.as_view(), name='ride_update'),
    path('<int:pk>/delete/', views.RideDeleteView.as_view(), name='ride_delete'),
    path('<int:ride_pk>/events/create/', views.CreateRideEventView.as_view(), name='rideevent_create'),
]
