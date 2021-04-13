import io

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from fifa.enums import ClubEnum, PlayerEnum
from fifa.import_models import ImportModel
from fifa.models import Club, Player
from fifa.serializers import ClubSerializer, PlayerSerializer


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
    ordering_fields = [PlayerEnum.NAME.value]

    def get_serializer_class(self):
        return PlayerSerializer

    @action(['post'], detail=False)
    @parser_classes([MultiPartParser])
    def upload(self, request):
        try:
            file = io.TextIOWrapper(request.FILES['file'], encoding='utf-8-sig')
        except KeyError:
            return Response({'file': 'Missing field'})

        return Response(ImportModel(file, self.get_serializer_class()).create())
