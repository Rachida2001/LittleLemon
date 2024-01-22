from django.shortcuts import render
#from requests import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication 
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()  
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all objects from the Booking model
    serializer_class = BookingSerializer  # Set the serializer class to BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
@api_view(['GET'])  # Define the HTTP method for this view
#@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])  # Uncomment this line if TokenAuthentication is required
def msg(request):
    return Response({"message": "This view is protected"})