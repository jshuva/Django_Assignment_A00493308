from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel, Reservation
from .serializers import HotelSerializer, ReservationSerializer
import random

class HotelListView(APIView):
    def get(self, request):
        checkin_date = request.query_params.get('checkin')
        checkout_date = request.query_params.get('checkout')
        
        hotels = Hotel.objects.all()
        
        # If dates are provided, filter out hotels that are booked for these dates
        if checkin_date and checkout_date:
            # Overlap condition: Reservation checkin < requested checkout AND Reservation checkout > requested checkin
            overlapping_reservations = Reservation.objects.filter(
                checkin__lt=checkout_date,
                checkout__gt=checkin_date
            )
            booked_hotel_names = overlapping_reservations.values_list('hotel_name', flat=True)
            hotels = hotels.exclude(name__in=booked_hotel_names)
        
        data = [{"hotel_name": h.name} for h in hotels]
        return Response(data, status=status.HTTP_200_OK)

class ReservationConfirmationView(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()
            return Response({"confirmation_number": reservation.confirmation_number}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
