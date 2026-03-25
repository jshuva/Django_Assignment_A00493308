from django.urls import path
from .views import HotelListView, ReservationConfirmationView

urlpatterns = [
    path('getListOfHotels', HotelListView.as_view(), name='get-hotels'),
    path('reservationConfirmation', ReservationConfirmationView.as_view(), name='reservation-confirmation'),
]
