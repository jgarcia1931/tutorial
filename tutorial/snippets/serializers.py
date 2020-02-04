from rest_framework import serializers
from .models import Snippet

from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'versionCont', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']
        read_only_fields = ['versionCont']

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'name', 'email', 'snippets']