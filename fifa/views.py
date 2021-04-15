import io
from datetime import datetime, timedelta

from django.db.models import DurationField, ExpressionWrapper, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from fifa.enums import ClubEnum, PlayerEnum
from fifa.import_models import ImportModel
from fifa.models import Club, Player
from fifa.serializers import ClubRetrieveSerializer, ClubSerializer, ImportPlayerSerializer, PlayerSerializer


class ClubViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows clubs to be viewed or edited. """
    queryset = Club.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = [e.value for e in ClubEnum]
    search_fields = [e.value for e in ClubEnum]
    ordering_fields = [e.value for e in ClubEnum]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClubRetrieveSerializer
        return ClubSerializer

    @action(['post'], detail=False)
    @parser_classes([MultiPartParser])
    def upload(self, request):
        try:
            file = io.TextIOWrapper(request.FILES['file'], encoding='utf-8-sig')
        except KeyError:
            return Response({'file': 'Missing field'})

        return Response(ImportModel(file, self.get_serializer_class()).create())


class PlayerViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows players to be viewed or edited. """
    queryset = Player.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = [PlayerEnum.NAME.value]
    search_fields = [PlayerEnum.NAME.value]
    ordering_fields = [PlayerEnum.NAME.value,
                       PlayerEnum.POTENTIAL.value,
                       PlayerEnum.JERSEY_NUMBER.value,
                       PlayerEnum.POSITION.value,
                       PlayerEnum.JOINED.value,
                       PlayerEnum.CONTRACT_VALID_UNTIL.value]

    def get_serializer_class(self):
        if self.action == 'upload':
            return ImportPlayerSerializer
        return PlayerSerializer

    def get_queryset(self):
        expression = ExpressionWrapper(F('contract_valid_until') - F('joined'), output_field=DurationField())
        qs = Player.objects.annotate(contract_length=expression)
        return qs

    @action(['get'], detail=True)
    def days_left_in_contract(self, request, pk=None):
        player = self.get_queryset().get(pk=pk)
        time_difference = player.contract_valid_until - datetime.today().astimezone()
        if time_difference < timedelta(days=0):
            return Response({"error": "contract expired"})
        else:
            return Response({"days": time_difference.days})

    @action(['post'], detail=False)
    @parser_classes([MultiPartParser])
    def upload(self, request):
        try:
            file = io.TextIOWrapper(request.FILES['file'], encoding='utf-8-sig')
        except KeyError:
            return Response({'file': 'Missing field'})

        return Response(ImportModel(file, self.get_serializer_class()).create())
