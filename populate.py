import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_reservation.settings')
django.setup()

from api.models import Hotel

def populate():
    hotels = [
        "The Grand Budapest Hotel",
        "Overlook Hotel",
        "Continental Hotel",
        "Bates Motel",
        "Fawlty Towers"
    ]
    for h in hotels:
        Hotel.objects.get_or_create(name=h)
    print("Populated dummy data.")

if __name__ == '__main__':
    populate()
