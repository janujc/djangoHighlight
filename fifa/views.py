from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from fifa.import_players import ImportPlayers
from fifa.models import Player, Club


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()


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
        super(PlayerViewSet, self).get_serializer_class()

    def get_parsers(self):
        if action == 'upload':
            return [MultiPartParser]
        else:
            super(PlayerViewSet, self).get_parsers()

    @action(['post'], detail=False)
    def upload(self, request):
        try:
            file = request.data['file']
        except KeyError:
            return Response({'file': 'Missing field'})

        return ImportPlayers(file).create()
