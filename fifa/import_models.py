import csv

from rest_framework.exceptions import ValidationError


class ImportClubs(object):
    def __init__(self, file=None, serializer=None):
        self.file = file
        self.reader = csv.DictReader(self.file)
        self.serializer = serializer

    def create(self):
        list_of_clubs = list(self.reader)
        for club in list_of_clubs:
            serializer = self.serializer(data=club)
            try:
                serializer.is_valid(raise_exception=True)
            except ValidationError as e:
                if e.detail == {"name": ["club with this name already exists."]}:
                    continue
                else:
                    raise e
            serializer.save()

        return 'success'


class ImportPlayers(object):
    def __init__(self, file=None, serializer=None):
        self.file = file
        self.reader = csv.DictReader(self.file)
        self.serializer = serializer

    def create(self):
        list_of_players = list(self.reader)
        print(list_of_players[28])
        serializer = self.serializer(data=list_of_players, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
