from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from .serializers import EmployeeSerializer
from .models import Employee
from .permissions import IsAdminOrReadOnly


class EmployeeList(APIView):

    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
