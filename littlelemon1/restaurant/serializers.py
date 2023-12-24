# serializers.py
from rest_framework import serializers
from .models import Menu
from .models import Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['ID', 'Title', 'Price', 'Inventory']  # Adjust fields as needed

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Assuming 'Booking' is the model name
        fields = '__all__'