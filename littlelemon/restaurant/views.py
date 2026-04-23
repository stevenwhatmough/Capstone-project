from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view, permission_classes
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message" : "This view is protected"})


class MenuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        item_name = str(serializer.instance)
        return Response({"message": f"{item_name} was added to the menu"}, status=status.HTTP_201_CREATED)

class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        item_name=str(instance)
        self.perform_destroy(instance)
        return Response({"message": f"{item_name} was removed from the menu"}, status=status.HTTP_200_OK)

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
