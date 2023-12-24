from django.db import models

class Menu(models.Model):
    # Define the fields for the Menu model
    ID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
  

    def __str__(self):
        return self.Title  

class Booking(models.Model):
    # Define the fields for the Booking model
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return f"Booking for {self.No_of_guests} people on {self.BookingDate}" 
