from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import permissions

# class SnippetSerializer(serializers.ModelSerializer):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Snippet
#         fields = ('id','title','code','linenos','language','style','owner')
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


# class UserSerializer(serializers.ModelSerializer):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
#     class Meta:
#         model = User
#         fields = ('id','username','snippets')
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
