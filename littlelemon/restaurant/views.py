from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_Classes = [permissions.IsAuthenticated]