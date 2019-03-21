from rest_framework import serializers
from .models import Members

class MembersSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
    class Meta:
        model = Members
        fields = ('id', 'name','email','interests', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')