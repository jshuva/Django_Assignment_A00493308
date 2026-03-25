from django.db import models
import uuid

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    confirmation_number = models.CharField(max_length=50, primary_key=True, editable=False)
    hotel_name = models.CharField(max_length=255)
    checkin = models.CharField(max_length=50)
    checkout = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
        if not self.confirmation_number:
            self.confirmation_number = str(uuid.uuid4())[:10].upper()
        super().save(*args, **kwargs)

class Guest(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='guests', on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    
    def __str__(self):
        return self.guest_name
