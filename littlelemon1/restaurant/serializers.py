# serializers.py
from rest_framework import serializers
from .models import Menu, MenuItem, Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['ID', 'Title', 'Price', 'Inventory']  # Adjust fields as needed

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Assuming 'Booking' is the model name
        fields = '__all__'
        

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']

    