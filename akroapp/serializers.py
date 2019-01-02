from django.contrib.auth.models import User, Group
from rest_framework import serializers
from akroapp.models import Exercise,Tag

class UserSerializer(serializers.HyperlinkedModelSerializer):
    exercises = serializers.HyperlinkedRelatedField(many=True, view_name='exercise-detail',read_only=True) 

    class Meta:
        model = User
        fields = ('url', 'username', 'email','exercises')


'''class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
'''
class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    creater = serializers.HyperlinkedRelatedField(many=False,view_name='user-detail', read_only=True,source='creater.id')
    tags = serializers.HyperlinkedRelatedField(many=True, queryset=Tag.objects.all(), view_name = 'tag-detail')
    class Meta:
        model = Exercise
        fields = ('url', 'id', 'name','description','tags','videourl','pictureurl','creater')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ( 'url', 'id', 'name')
