from rest_framework.views import APIView
from datetime import date
from rest_framework.response import Response
from rest_framework import status
from .models import Vote
from .serializers import VoteSerializer


class VoteResultsAPIView(APIView):
    def get(self, request, menu_id, format=None):
        today = date.today()
        votes = Vote.objects.filter(menu_id=menu_id, date=today)
        if votes:
            serializer = VoteSerializer(votes, many=True)
            return Response(serializer.data)
        return Response({'message': 'No votes found for this menu'}, status=status.HTTP_404_NOT_FOUND)
