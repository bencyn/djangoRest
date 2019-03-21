from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MembersSerializer
from .models import Members

# Create your views here.

class MembersViewSet(viewsets.ModelViewSet):
    """API endpoint that allows members to be viewed or edited.
    """

    queryset = Members.objects.all()
    serializer_class=MembersSerializer

    def perform_create(self,serializer):
        """Save the post data when creating a new member."""
        serializer.save()