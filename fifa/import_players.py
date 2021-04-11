class ImportPlayers(object):
    def __init__(self, file=None):
        self.file = file

    @property
    def file(self):
        return self.file

    @file.setter
    def file(self, value):
        if value is None:
            raise ValueError({'file': 'Must not be None'})
        else:
            self.file = value

    def create(self):
        pass
