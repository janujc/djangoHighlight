import io

from rest_framework import viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from fifa.enums import ClubEnum
from fifa.import_models import ImportClubs, ImportPlayers
from fifa.models import Player, Club
from fifa.serializers import ClubSerializer, PlayerSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    search_fields = [
        ClubEnum.NAME.value,
    ]

    def get_serializer_class(self):
        return ClubSerializer

    @action(['post'], detail=False)
    @parser_classes([MultiPartParser])
    def upload(self, request):
        try:
            file = io.TextIOWrapper(request.FILES['file'], encoding='utf-8-sig')
        except KeyError:
            return Response({'file': 'Missing field'})

        return Response(ImportClubs(file, self.get_serializer_class()).create())


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all()
    filterset_fields = [

    ]
    search_fields = [

    ]
    ordering_fields = [

    ]

    def get_serializer_class(self):
        return PlayerSerializer

    @action(['post'], detail=False)
    @parser_classes([MultiPartParser])
    def upload(self, request):
        try:
            file = io.TextIOWrapper(request.FILES['file'], encoding='utf-8-sig')
        except KeyError:
            return Response({'file': 'Missing field'})

        return Response(ImportPlayers(file, self.get_serializer_class()).create())
