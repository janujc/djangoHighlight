from csv import DictReader


class ImportModel(object):
    def __init__(self, file=None, serializer=None):
        self.file = file
        self.reader = DictReader(self.file)
        self.serializer = serializer

    def create(self):
        objs = list(self.reader)
        serializer = self.serializer(data=objs, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
