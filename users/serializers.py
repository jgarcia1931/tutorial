from rest_framework import serializers
from .models import CustomUser
import sys
sys.path.append('../')
from snippets import Snippet


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'email', 'snippets']