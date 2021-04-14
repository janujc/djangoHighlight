from rest_framework import serializers

from fifa.enums import ClubEnum, PlayerEnum
from fifa.fields import EuroField, HeightField, WeightField
from fifa.models import Club, Player


class ImportPlayerSerializer(serializers.ModelSerializer):
    club = serializers.SlugRelatedField(queryset=Club.objects.all(), slug_field='name', allow_null=True)
    value = EuroField()
    wage = EuroField()
    joined = serializers.DateField(format='%Y-%m-%d', input_formats=['%d-%b-%y', ''], allow_null=True)
    contract_valid_until = serializers.DateField(format='%Y-%m-%d', input_formats=['%d-%b-%y', '%Y', ''], allow_null=True)
    loaned_from = serializers.SlugRelatedField(queryset=Club.objects.all(), slug_field='name', allow_null=True)
    height = HeightField()
    weight = WeightField()

    class Meta:
        model = Player
        fields = ['pk'] + [e.value for e in PlayerEnum]

    def to_internal_value(self, data):
        if data['joined'] == '':
            data['joined'] = None
        if data['contract_valid_until'] == '':
            data['contract_valid_until'] = None
        return super(ImportPlayerSerializer, self).to_internal_value(data)


class PlayerSerializer(serializers.ModelSerializer):
    club = serializers.SlugRelatedField(queryset=Club.objects.all(), slug_field='name', allow_null=True)
    joined = serializers.DateField(format='%Y-%m-%d', input_formats=['%d-%b-%y', '%Y-%m-%d', ''], allow_null=True)
    contract_valid_until = serializers.DateField(format='%Y-%m-%d', input_formats=['%d-%b-%y', '%Y', '%Y-%m-%d', ''], allow_null=True)
    loaned_from = serializers.SlugRelatedField(queryset=Club.objects.all(), slug_field='name', allow_null=True)
    height = HeightField()
    weight = WeightField()

    class Meta:
        model = Player
        fields = ['pk'] + [e.value for e in PlayerEnum]

    def to_internal_value(self, data):
        if data['joined'] == '':
            data['joined'] = None
        if data['contract_valid_until'] == '':
            data['contract_valid_until'] = None
        return super(PlayerSerializer, self).to_internal_value(data)


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['pk'] + [e.value for e in ClubEnum]
