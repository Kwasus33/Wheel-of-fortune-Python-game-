from Utilities import read_from_csv, read_from_json
import os.path


class PersonPathNotFound(FileNotFoundError):
    pass


class PersonPermissionError(PermissionError):
    pass


class PersonPathIsDirectory(IsADirectoryError):
    pass


class Database():
    def __init__(self) -> None:
        self.people = []

    def load_from_file(self, path):
        ext = os.path.splitext(path)[:-1]
        try:
            with open(path, 'r') as file_handle:
                if ext == 'json':
                    self.people = read_from_json(file_handle)
                else:
                    self.people = read_from_csv(file_handle)
        except FileNotFoundError:
            raise PersonPathNotFound("Could not open person database")
        except PermissionError:
            msg = 'You do not have permission to open the database'
            raise PersonPermissionError(msg)
        except IsADirectoryError:
            raise PersonPathIsDirectory('Can only work on files')
