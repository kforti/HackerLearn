from pathlib import Path



class CSVResourceEntryDAO:
    def __init__(self, entry_path):
        self.entry_path = Path(entry_path)

    def add(self, data):
        pass

    def get(self, id):
        pass


class CSVResourceDAO:
    def __init__(self, path):
        self.path = Path(path)


