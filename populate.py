import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_reservation.settings')
django.setup()

from api.models import Hotel, Reservation, Guest

def populate():
    # Clear existing data so we don't end up with hundreds of duplicates if run multiple times
    Hotel.objects.all().delete()
    Reservation.objects.all().delete()

    hotel_names = [
        "The Grand Budapest Hotel",
        "Overlook Hotel",
        "Continental Hotel",
        "Bates Motel",
        "Fawlty Towers"
    ]
    
    # 1. Create Hotels
    hotels = []
    for h in hotel_names:
        hotel, created = Hotel.objects.get_or_create(name=h)
        hotels.append(hotel)
        
    print(f"Created {len(hotels)} dummy Hotels.")

    # 2. Create some dummy Reservations and Guests
    for i in range(3):
        res = Reservation.objects.create(
            hotel_name=random.choice(hotel_names),
            checkin=(datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"),
            checkout=(datetime.now() + timedelta(days=i+3)).strftime("%Y-%m-%d"),
        )
        
        # Add 1 or 2 guests to the reservation
        Guest.objects.create(
            reservation=res,
            guest_name=f"Dummy Guest {i}A",
            gender="Female" if i % 2 == 0 else "Male"
        )
        if random.choice([True, False]):
            Guest.objects.create(
                reservation=res,
                guest_name=f"Dummy Guest {i}B",
                gender="Male" if i % 2 == 0 else "Female"
            )
            
    print(f"Created 3 dummy Reservations with assorted Guests.")

if __name__ == '__main__':
    populate()
