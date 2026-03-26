from django.contrib import admin
from .models import Hotel, Reservation, Guest

class GuestInline(admin.TabularInline):
    model = Guest
    extra = 1

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('confirmation_number', 'hotel_name', 'checkin', 'checkout')
    search_fields = ('confirmation_number', 'hotel_name')
    inlines = [GuestInline]

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'gender', 'reservation')
    search_fields = ('guest_name',)
