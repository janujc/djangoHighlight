from rest_framework import serializers

from fifa.enums import ClubEnum, PlayerEnum
from fifa.fields import EuroField, HeightField, WeightField
from fifa.models import Club, Player


class PlayerSerializer(serializers.ModelSerializer):
    club = serializers.SlugRelatedField(queryset=Club.objects.all(), slug_field='name', allow_null=True)
    value = EuroField()
    wage = EuroField()
    joined = serializers.DateField(format="%Y-%m-%d", input_formats=["%d-%b-%y", ""])
    contract_valid_until = serializers.DateField(format="%Y-%m-%d", input_formats=["%d-%b-%y", "%Y", ""])
    loaned_from = serializers.SlugRelatedField(queryset=Club.objects.all(), slug_field='name', allow_null=True)
    height = HeightField()
    weight = WeightField()

    class Meta:
        model = Player
        fields = [e.value for e in PlayerEnum]


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = [e.value for e in ClubEnum]
