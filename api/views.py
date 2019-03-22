from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeamsSerializer
from .models import Teams

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    """API endpoint that allows members to be viewed or edited.
    """

    queryset = Teams.objects.all()
    serializer_class=TeamsSerializer

    def perform_create(self,serializer):
        """Save the post data when creating a new member."""
        serializer.save()