from rest_framework import (
    serializers,
)

from . import models
from . import utils


class PersonSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = models.Person
        fields = ['id', 'username', 'age', 'fruits', 'vegetables']

    def get_username(self, obj):
        return obj.name


class BasePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'name', 'age', 'address', 'phone']


class MutualFriendSerializer(serializers.Serializer):
    persons = serializers.ListField(child=serializers.CharField(), write_only=True)
    persons_info = serializers.ListField(child=BasePersonSerializer(), read_only=True)
    friends = serializers.ListField(child=serializers.IntegerField(), read_only=True)

    def create(self, validated_data):
        wants = models.Person.objects.filter(id__in=validated_data['persons'])
        friends = []
        for want in wants:
            friends.append(want.friends.values_list('id', flat=True))

        mutuals_ids = utils.common_section(friends)
        final = models.Person.objects.filter(id__in=mutuals_ids, has_died=False, eye_color=models.Person.EYE_COLOR_BROWN).values_list('id', flat=True)

        return {
            'persons_info': wants,
            'friends': final,
        }
