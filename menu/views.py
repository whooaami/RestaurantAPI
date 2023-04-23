from rest_framework import status
from datetime import date
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Menu
from restaurant.models import Restaurant
from .serializers import MenuSerializer
from .permissions import IsAdminOrReadOnly


class MenuList(APIView):

    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, format=None):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MenuUpload(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        menu = get_object_or_404(Menu.objects.all(), pk=pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(id=pk)
        except Restaurant.DoesNotExist:
            return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        menu = Menu.objects.create(restaurant=restaurant, **serializer.validated_data)
        menu.save()
        return Response({'message': 'Menu uploaded successfully'}, status=status.HTTP_201_CREATED)


class MenuDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        menu = get_object_or_404(Menu.objects.all(), pk=pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        menu = get_object_or_404(Menu.objects.all(), pk=pk)
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        menu = get_object_or_404(Menu.objects.all(), pk=pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CurrentDayMenu(APIView):
    def get(self, request, restaurant_id, format=None):
        today = date.today()
        menus = Menu.objects.filter(restaurant_id=restaurant_id, date=today)
        if menus:
            serializer = MenuSerializer(menus, many=True)
            return Response(serializer.data)
        return Response({'message': 'No menu found for this restaurant on this day'}, status=status.HTTP_404_NOT_FOUND)
