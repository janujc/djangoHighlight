import datetime

from django.utils.dateparse import parse_duration
from rest_framework import serializers
from decimal import *


class HeightField(serializers.Field):
    """ heights are serialized from a modified imperial shorthand to inches """
    def to_representation(self, value):
        inches = value % 12
        feet = (value - inches) // 12
        return f'{feet}\'{inches}'

    def to_internal_value(self, data):
        data = data.split('\'')
        feet = data[0]
        inches = data[1]
        return int(feet) * 12 + int(inches)


class WeightField(serializers.Field):
    """ weights are serialized from a string to integer """
    def to_representation(self, value):
        return f'{value}lbs'

    def to_internal_value(self, data):
        return int(data.rstrip('lbs'))


class EuroField(serializers.Field):
    """ euro shorthand serialized from a string to an integer """
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        if data[-1] == '0':
            return Decimal(0)
        else:
            digits = Decimal(data[1:-1])
            multiplier = data[-1]
            if multiplier == 'K':
                return digits * Decimal(1000)
            elif multiplier == 'M':
                return digits * Decimal(1000000)
            else:
                return digits


class CustomDurationField(serializers.DurationField):
    """ DurationField but only returns number of days """
    def to_representation(self, value):
        if isinstance(value, datetime.timedelta):
            return f'{value.days} days'
        parsed = parse_duration(str(value))
        if parsed is not None:
            return f'{parsed.days} days'
        self.fail('invalid', format='[DD] [HH:[MM:]]ss[.uuuuuu]')
