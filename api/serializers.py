from rest_framework import serializers
from .models import Hotel, Reservation, Guest

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name']

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guest_name', 'gender']

class ReservationSerializer(serializers.ModelSerializer):
    guests_list = GuestSerializer(many=True, source='guests')
    
    class Meta:
        model = Reservation
        fields = ['hotel_name', 'checkin', 'checkout', 'guests_list']
        
    def create(self, validated_data):
        guests_data = validated_data.pop('guests')
        reservation = Reservation.objects.create(**validated_data)
        for guest_data in guests_data:
            Guest.objects.create(reservation=reservation, **guest_data)
        return reservation
