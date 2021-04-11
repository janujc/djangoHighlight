from rest_framework import serializers

from fifa.enums import PlayerEnum
from fifa.models import Club, Player


class PlayerSerializer(serializers.ModelSerializer):
    club = serializers.SlugRelatedField(queryset=Club.objects.all(), slug_field='name', required=False)

    class Meta:
        model = Player
        fields = [e.value for e in PlayerEnum]
